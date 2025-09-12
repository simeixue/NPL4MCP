#!/bin/sh
set -e
LC_ALL=C

REPOS_DIR="/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE="/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg"

command -v code2flow >/dev/null 2>&1 || { echo "缺少 code2flow：pip install code2flow" >&2; exit 1; }

for PROJ in "${REPOS_DIR}"/*; do
  [ -d "${PROJ}" ] || continue
  NAME=$(basename "${PROJ}")
  OUT="${OUT_BASE}/${NAME}"
  mkdir -p "${OUT}"

  ########################
  # Python -> cg_py.json
  ########################
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
  -print > "${PY_TMP}"


  if [ -s "${PY_TMP}" ]; then
    echo "[py ] ${NAME} -> ${OUT}/cg_py.json"
    if ! xargs code2flow --language py -o "${OUT}/cg_py.json" < "${PY_TMP}" >/dev/null 2> "${OUT}/.py.err"; then
      echo "[warn] Python 解析失败: ${NAME}；错误日志见 ${OUT}/.py.err"
    fi
  else
    echo "[skip py ] ${NAME} 无 .py 文件"
  fi
  rm -f "${PY_TMP}"
done

echo "[done]"
