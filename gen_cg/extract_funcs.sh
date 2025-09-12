#!/bin/sh
set -e
LC_ALL=C

REPOS_DIR="/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE="/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg"

mkdir -p "$OUT_BASE"

for PROJ in "${REPOS_DIR}"/*; do
  [ -d "${PROJ}" ] || continue
  NAME=$(basename "${PROJ}")
  OUT_DIR="${OUT_BASE}/${NAME}/func_implement"
  mkdir -p "${OUT_DIR}"

    PY_TMP=$(mktemp)
  find "${PROJ}" -type f -name '*.py' \
    -not -name '__init__.py' \
    -not -path '*/.git/*' \
    -not -path '*/__pycache__/*' \
    -not -path '*/.mypy_cache/*' \
    -not -path '*/.pytest_cache/*' \
    -not -path '*/site-packages/*' \
    -not -path '*/venv/*' \
    -not -path '*/.venv/*' \
    -not -path '*/env/*' \
    -not -path '*/test/*' \
    -print > "${PY_TMP}"

  COUNT=$(wc -l < "${PY_TMP}" | tr -d ' ')
  echo "[funcs] ${NAME}: ${COUNT} py files -> ${OUT_DIR}"

  python3 - "${PROJ}" "${OUT_DIR}" "${PY_TMP}" <<'PY'
import sys, os, io, ast, re

proj_root = os.path.abspath(sys.argv[1])
out_dir   = os.path.abspath(sys.argv[2])
list_path = sys.argv[3]

with io.open(list_path, "r", encoding="utf-8", errors="ignore") as f:
    files = [line.strip() for line in f if line.strip()]

os.makedirs(out_dir, exist_ok=True)

def rel_module(path):
    rel = os.path.relpath(path, proj_root)
    mod = os.path.splitext(rel)[0].replace(os.sep, ".")
    return re.sub(r'^\.+', '', mod)

name_counts = {}

def safe_basename(qname):
    base = qname.split(".")[-1]
    base = re.sub(r'[^0-9A-Za-z_]+', '_', base) or "func"
    i = name_counts.get(base, 0)
    name_counts[base] = i + 1
    return f"{base}.py" if i == 0 else f"{base}_{i}.py"

def write_func(qname, module, path, node, lines):
    if hasattr(node, "lineno") and hasattr(node, "end_lineno"):
        start, end = node.lineno, node.end_lineno
        body = "\n".join(lines[start-1:end])
    else:
        body = lines[node.lineno-1] if hasattr(node,"lineno") else f"def {qname.split('.')[-1]}():\n    pass"
    out_path = os.path.join(out_dir, safe_basename(qname))
    header = [
        f"# file: {os.path.abspath(path)}",
        f"# module: {module}",
        f"# qname: {qname}",
        f"# lines: {getattr(node,'lineno',0)}-{getattr(node,'end_lineno',0)}",
        ""
    ]
    with io.open(out_path, "w", encoding="utf-8") as w:
        w.write("\n".join(header) + body)

for path in files:
    try:
        with io.open(path, "r", encoding="utf-8") as f:
            src = f.read()
    except Exception:
        try:
            with io.open(path, "r", encoding="utf-8", errors="ignore") as f:
                src = f.read()
        except Exception:
            continue
    try:
        tree = ast.parse(src, filename=path)
    except Exception:
        continue

    module = rel_module(path)
    lines = src.splitlines()

    parents = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent

    def qname(n):
        parts = [getattr(n, "name", "")]
        cur = n
        while cur in parents:
            cur = parents[cur]
            if isinstance(cur, ast.ClassDef):
                parts.append(cur.name)
            if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef)):
                parts.append(cur.name)
        parts = list(reversed(parts))
        return f"{module}." + ".".join(parts) if module else ".".join(parts)

    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            write_func(qname(n), module, path, n, lines)
PY

  rm -f "${PY_TMP}"
done

echo "[done]"
