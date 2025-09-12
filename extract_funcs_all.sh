#!/bin/sh
set -e
LC_ALL=C

# 用法:
#   ./extract_funcs_all_v2.sh [BASE_DIR]
BASE="${1:-/Users/xue/workspace/mcp_project/mcp_server_repos}"

command -v python3 >/dev/null 2>&1 || { echo "缺少 python3" >&2; exit 1; }
command -v node    >/dev/null 2>&1 || { echo "缺少 node" >&2; exit 1; }
command -v npm     >/dev/null 2>&1 || { echo "缺少 npm"  >&2; exit 1; }

TOOLS="${HOME}/.func_extract_tools_v2"; mkdir -p "${TOOLS}/py" "${TOOLS}/js"

# -------- Python 提取器（更稳，完整遍历 + 祖先栈生成限定名） --------
cat > "${TOOLS}/py/extract_py_funcs.py" <<'PY'
#!/usr/bin/env python3
import ast, os, sys, pathlib
BASE = sys.argv[1] if len(sys.argv) > 1 else "."
OUT  = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, "func_extract_py")
SKIP = ("/.git/", "/__pycache__/", "/.venv/", "/venv/", "/env/", "/site-packages/")

def sanitize(s): return "".join(c if c.isalnum() or c in "._-" else "_" for c in s)
def read_text(p):
    for enc in ("utf-8","utf-8-sig","latin-1"):
        try: return pathlib.Path(p).read_text(encoding=enc)
        except: pass
    return None

def build_parent(root):
    parent = {}
    for n in ast.walk(root):
        for c in ast.iter_child_nodes(n): parent[c]=n
    return parent

def qname(node, parent):
    parts=[]; cur=node
    while cur in parent:
        cur = parent[cur]
        if isinstance(cur,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            parts.append(cur.name)
    return ".".join(reversed(parts + [node.name]))

def bounds(node):
    decos = getattr(node,"decorator_list",[]) or []
    start = min([getattr(d,"lineno",node.lineno) for d in decos] + [node.lineno])
    end   = getattr(node,"end_lineno",node.lineno)
    return start,end

def write(rel, qn, s, e, lines):
    out_dir = os.path.join(OUT, os.path.dirname(rel)); os.makedirs(out_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(rel))[0]
    fn = f"{base}__{sanitize(qn)}__L{s}-L{e}.py"
    pathlib.Path(out_dir, fn).write_text("".join(lines[s-1:e]), encoding="utf-8")

def main():
    for root,_,files in os.walk(BASE):
        rp = root.replace("\\","/")
        if any(x in rp for x in SKIP): continue
        for f in files:
            if not f.endswith(".py"): continue
            p = os.path.join(root,f); src = read_text(p)
            if not src: continue
            try: tree = ast.parse(src)
            except SyntaxError: continue
            parent = build_parent(tree)
            lines = src.splitlines(keepends=True)
            for n in ast.walk(tree):
                if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
                    s,e = bounds(n)
                    write(os.path.relpath(p,BASE), qname(n,parent), s,e, lines)
if __name__=="__main__": main()
PY
chmod +x "${TOOLS}/py/extract_py_funcs.py"

# -------- JS/TS 提取器（Babel，含类字段箭头、export default 等） --------
if [ ! -d "${TOOLS}/js/node_modules" ]; then
  ( cd "${TOOLS}/js" && npm init -y >/dev/null \
    && npm i @babel/parser @babel/traverse fast-glob >/dev/null )
fi
cat > "${TOOLS}/js/extract_js_ts_funcs.mjs" <<'JS'
#!/usr/bin/env node
import fs from "node:fs"; import path from "node:path";
import fg from "fast-glob"; import {parse} from "@babel/parser";
import traverseMod from "@babel/traverse"; const traverse=traverseMod.default||traverseMod;

const BASE=process.argv[1+1]||"."; const OUT=process.argv[2+1]||path.join(BASE,"func_extract_js");
const parserOpts={sourceType:"unambiguous",allowReturnOutsideFunction:true,plugins:[
  "typescript","jsx","classProperties","classPrivateProperties","classPrivateMethods",
  ["decorators",{decoratorsBeforeExport:false}],
  "dynamicImport","objectRestSpread","optionalChaining","nullishCoalescingOperator",
  "topLevelAwait","importMeta","exportDefaultFrom","exportNamespaceFrom"
]};
const sanitize=s=>s.replace(/[^a-zA-Z0-9._-]/g,"_");
function lineOf(src,i){let n=1;for(let k=0;k<i;k++) if(src.charCodeAt(k)===10)n++;return n;}
function write(rel,name,s,e,src){
  const od=path.join(OUT,path.dirname(rel)); fs.mkdirSync(od,{recursive:true});
  const base=path.parse(path.basename(rel)).name;
  const fn=`${base}__${sanitize(name)}__L${lineOf(src,s)}-L${lineOf(src,e)}.js`;
  fs.writeFileSync(path.join(od,fn),src.slice(s,e),"utf8");
}
function className(p){
  const k=p.findParent(pp=>pp.isClassDeclaration()||pp.isClassExpression());
  return k?.node.id?.name || "Class";
}
function funcName(p){
  const n=p.node;
  if(n.id?.name) return n.id.name; // function foo(){}
  const pd=p.parentPath;
  if(pd?.isVariableDeclarator() && pd.node.id.type==="Identifier") return pd.node.id.name; // const foo=...
  if(pd?.isAssignmentExpression()) return p.parentPath.get("left").toString(); // a.b=...
  if(pd?.isObjectProperty() || pd?.isObjectMethod()){
    const key=pd.node.key; return key.type==="Identifier"?key.name:pd.get("key").toString();
  }
  if(p.isClassMethod()||p.isClassPrivateMethod()){
    const mkey=p.node.key; const mn=mkey.type==="Identifier"?mkey.name:p.get("key").toString();
    return `${className(p)}.${mn}`;
  }
  if(p.findParent(pp=>pp.isExportDefaultDeclaration())) return "export_default";
  return `anonymous_${lineOf(p.hub.file.code, n.start||0)}`;
}
function rangeWithDecoratorsOrInit(p){
  let s=p.node.start,e=p.node.end;
  const dec=p.node.decorators||[]; if(dec.length) s=Math.min(s,...dec.map(d=>d.start));
  const pp=p.parentPath;
  if(pp?.isVariableDeclarator()||pp?.isObjectProperty()||pp?.isObjectMethod()||pp?.isAssignmentExpression()) s=Math.min(s,pp.node.start);
  return [s,e];
}
async function main(){
  const entries=await fg(["**/*.{js,jsx,ts,tsx}"],{cwd:BASE,dot:false,ignore:["**/node_modules/**","**/.git/**"]});
  for(const rel of entries){
    const abs=path.join(BASE,rel); let code=fs.readFileSync(abs,"utf8"); if(code.startsWith("#!")) code="// "+code;
    let ast; try{ast=parse(code,parserOpts);}catch{continue;}
    const seen=new Set();
    const emit=(p,nm,s,e)=>{const k=rel+"\0"+s+"\0"+e; if(seen.has(k)) return; seen.add(k); write(rel,nm,s,e,code);};
    const visit= p => { const nm=funcName(p); const [s,e]=rangeWithDecoratorsOrInit(p); emit(p,nm,s,e); };

    traverse(ast,{
      FunctionDeclaration:visit, FunctionExpression:visit, ArrowFunctionExpression:visit,
      ObjectMethod:visit, ClassMethod:visit, ClassPrivateMethod:visit,
      // 类字段箭头函数: method = () => {}
      ClassProperty(p){ const v=p.node.value; if(v && (v.type==="ArrowFunctionExpression"||v.type==="FunctionExpression")){
        const nm=`${className(p)}.${(p.node.key.type==="Identifier"?p.node.key.name:p.get("key").toString())}`;
        const s=p.node.start, e=p.node.end; // 包含 "name = () => {}"
        emit(p,nm,s,e);
      }},
      ClassPrivateProperty(p){ const v=p.node.value; if(v && (v.type==="ArrowFunctionExpression"||v.type==="FunctionExpression")){
        const nm=`${className(p)}.${p.get("key").toString()}`;
        emit(p,nm,p.node.start,p.node.end);
      }},
      // export default () => {}
      ExportDefaultDeclaration(p){
        const d=p.node.declaration;
        if(d && (d.type==="FunctionDeclaration"||d.type==="FunctionExpression"||d.type==="ArrowFunctionExpression")){
          const s=d.start, e=d.end; write(rel,"export_default",s,e,code);
        }
      }
    });
  }
}
main();
JS
chmod +x "${TOOLS}/js/extract_js_ts_funcs.mjs"

echo "[scan] ${BASE}"
for PROJ in "${BASE}"/*; do
  [ -d "${PROJ}" ] || continue
  echo "[run ] $(basename "${PROJ}")"
  python3 "${TOOLS}/py/extract_py_funcs.py" "${PROJ}" "${PROJ}/func_extract_py" || true
  ( cd "${TOOLS}/js" && node "./extract_js_ts_funcs.mjs" "${PROJ}" "${PROJ}/func_extract_js" ) || true
done
echo "[done] 结果在各项目 func_extract_py/ 与 func_extract_js/ 下"
