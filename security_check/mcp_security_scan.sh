#!/usr/bin/env bash
set -euo pipefail

# 用法：
# chmod +x security_check/mcp_security_scan.sh
# 1) 扫描每个 mcp server 项目（依赖+代码）：
#    ./security_check/mcp_security_scan.sh repo /Users/xue/workspace/mcp_project/mcp_server_pyrepos
# 2) 扫描每个 tools_with_impl.json 中实现对应的源文件（仅代码）：
#    ./security_check/mcp_security_scan.sh json-root /Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg
#    （会自动遍历 <project>/tools_with_impl.json）
#
# 输出在 OUT_ROOT="./security_check/security_reports" 下
# 依赖：pip install pip-audit bandit semgrep
# 可选：poetry（若项目用 pyproject.toml）

MODE="${1:-}"
TARGET="${2:-}"
[ -z "$MODE" ] && { echo "missing mode"; exit 1; }
[ -z "$TARGET" ] && { echo "missing target"; exit 1; }

for t in pip-audit bandit semgrep; do
  command -v "$t" >/dev/null 2>&1 || { echo "请先安装: pip install pip-audit bandit semgrep"; exit 1; }
done

OUT_ROOT="./security_check/security_reports"
TS=$(date +"%Y%m%d-%H%M%S")
mkdir -p "$OUT_ROOT"

run_pip_audit() {
  local proj_dir="$1" out_dir="$2"
  local out="$out_dir/pip_audit.json"
  if [ -f "$proj_dir/requirements.txt" ]; then
    pip-audit -r "$proj_dir/requirements.txt" --format json -o "$out" || true
  elif [ -f "$proj_dir/pyproject.toml" ] && command -v poetry >/dev/null 2>&1; then
    poetry export -f requirements.txt --without-hashes -o "$out_dir/.req.txt"
    pip-audit -r "$out_dir/.req.txt" --format json -o "$out" || true
    rm -f "$out_dir/.req.txt"
  else
    pip-audit --format json -o "$out" || true
  fi
}


run_static_scan() {
  local path="$1" out_dir="$2"
  mkdir -p "$out_dir"
  bandit -r "$path" -f json -o "$out_dir/bandit.json" || true
  semgrep --config auto --json --output "$out_dir/semgrep.json" "$path" || true
}

summarize() {
  python - "$1" <<'PY'
import json, os, sys
d=sys.argv[1]
def jload(p):
    try: return json.load(open(p))
    except: return {}
pa=jload(os.path.join(d,"pip_audit.json"))
bd=jload(os.path.join(d,"bandit.json"))
sg=jload(os.path.join(d,"semgrep.json"))
print(f"summary: pip-audit={len(pa.get('vulnerabilities',[]))}, bandit={len(bd.get('results',[]))}, semgrep={len(sg.get('results',[]))}")
print(f"[saved] {d}")
PY
}

extract_files_from_tools_json() {
  # 从 tools_with_impl.json 中所有 depth_* 代码块的首行 "# file: <path>" 提取唯一路径
  local json_path="$1"
  python - "$json_path" <<'PY'
import json, re, sys
p=sys.argv[1]
data=json.load(open(p))
paths=set()
def scan_block(s):
    if not isinstance(s,str): return
    m=re.search(r'^#\s*file:\s*(.+)$', s.strip().split('\n')[0])
    if m: paths.add(m.group(1).strip())
def walk(x):
    if isinstance(x, dict):
        for k,v in x.items():
            if k.startswith('depth_'):  # depth_0 / depth_1 ...
                if isinstance(v, list):
                    for it in v: scan_block(it)
                else:
                    scan_block(v)
            else:
                walk(v)
    elif isinstance(x, list):
        for it in x: walk(it)
walk(data)
for p in sorted(paths): print(p)
PY
}

case "$MODE" in
  repo)
    REPO_BASE="$TARGET"
    [ -d "$REPO_BASE" ] || { echo "目录不存在: $REPO_BASE"; exit 1; }
    for proj in "$REPO_BASE"/*; do
        [ -d "$proj" ] || continue
        name="$(basename "$proj")"
        out="$OUT_ROOT/repo-${name}-$TS"
        echo "[repo] $name"

        (
            set +e
            mkdir -p "$out"
            run_pip_audit "$proj" "$out"
            bandit -r "$proj" -f json -o "$out/bandit.json" || true
            semgrep --config auto --json --output "$out/semgrep.json" "$proj" || true
        )
        summarize "$out"
    done

    ;;

  json-root)
    ROOT="$TARGET"
    [ -d "$ROOT" ] || { echo "目录不存在: $ROOT"; exit 1; }
    # 遍历 <project>/tools_with_impl.json
    find "$ROOT" -type f -name 'tools_with_impl.json' | while read -r jf; do
      proj="$(basename "$(dirname "$jf")")"
      echo "[json] $proj -> $jf"
      # 提取唯一文件路径
      mapfile -t files < <(extract_files_from_tools_json "$jf")
      if [ "${#files[@]}" -eq 0 ]; then
        echo "  无可扫描文件"
        continue
      fi
      out="$OUT_ROOT/json-${proj}-$TS"
      mkdir -p "$out/src"
      # 把文件复制到 out/src 保证扫描稳定，避免跨仓库相对导入问题
      ok=0
      for f in "${files[@]}"; do
        if [ -f "$f" ]; then
          cp "$f" "$out/src/$(echo "$f" | sed 's#/#__#g')"
          ok=1
        else
          echo "  [warn] missing: $f"
        fi
      done
      if [ "$ok" -eq 1 ]; then
        run_static_scan "$out/src" "$out"
        summarize "$out"
      else
        echo "  [skip] 没有存在的源文件"
      fi
    done
    ;;

  *)
    echo "未知模式: $MODE"
    exit 1
    ;;
esac

echo "ALL DONE -> $OUT_ROOT/"
