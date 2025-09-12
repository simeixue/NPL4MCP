#!/bin/sh
set -e
LC_ALL=C

# 用法: ./code2flow_py_js.sh [BASE_DIR]
BASE="${1:-/Users/xue/workspace/mcp_project/mcp_server_repos}"

command -v code2flow >/dev/null 2>&1 || { echo "缺少 code2flow：pip install code2flow" >&2; exit 1; }

for PROJ in "${BASE}"/*; do
  [ -d "${PROJ}" ] || continue
  NAME=$(basename "${PROJ}")
  OUT="${PROJ}/callgraph"; mkdir -p "${OUT}"

  ########################
  # Python -> cg_py.json
  ########################
  PY_TMP=$(mktemp)
  find "${PROJ}" -type f -name '*.py' \
    -not -path '*/.git/*' \
    -not -path '*/__pycache__/*' \
    -not -path '*/.mypy_cache/*' \
    -not -path '*/.pytest_cache/*' \
    -not -path '*/site-packages/*' \
    -not -path '*/venv/*' \
    -not -path '*/.venv/*' \
    -not -path '*/env/*' -print0 > "${PY_TMP}"

  if [ -s "${PY_TMP}" ]; then
    echo "[py ] ${NAME} -> ${OUT}/cg_py.json"
    if ! xargs -0 code2flow --language py -o "${OUT}/cg_py.json" < "${PY_TMP}" >/dev/null 2> "${OUT}/.py.err"; then
      echo "[warn] py失败: ${NAME}；看 ${OUT}/.py.err"
    fi
  else
    echo "[skip py ] ${NAME} 无 .py"
  fi
  rm -f "${PY_TMP}"

  ########################
  # JS/TS -> cg_js.json
  ########################
  JS_LIST=$(mktemp)
  find "${PROJ}" -type f \( -name '*.js' -o -name '*.jsx' -o -name '*.ts' -o -name '*.tsx' \) \
    -not -path '*/.git/*' \
    -not -path '*/node_modules/*' -print0 > "${JS_LIST}"

  if [ -s "${JS_LIST}" ]; then
    echo "[js ] ${NAME} -> ${OUT}/cg_js.json"

    # 尝试用 esbuild 先把 TS/TSX 转成 JS（同时可处理 JS/JSX）
    ESFAIL=0
    TMPJS=""
    if command -v npx >/dev/null 2>&1; then
      TMPJS=$(mktemp -d)
      TSCONF=""
      [ -f "${PROJ}/tsconfig.json" ] && TSCONF="--tsconfig=${PROJ}/tsconfig.json"

      if ! xargs -0 npx -y esbuild \
            --format=esm --platform=node --target=es2019 \
            --log-level=warning --outdir="${TMPJS}" \
            --loader:.ts=ts --loader:.tsx=tsx --loader:.jsx=jsx ${TSCONF} \
            < "${JS_LIST}" >/dev/null 2>"${OUT}/.esbuild.err"; then
        ESFAIL=1
      fi
    else
      ESFAIL=1
    fi

    if [ "${ESFAIL}" -eq 0 ]; then
      # 去除转译产物中的 shebang
      find "${TMPJS}" -type f \( -name '*.js' -o -name '*.jsx' \) -print0 \
        | while IFS= read -r -d '' f; do
            awk 'NR==1 && /^#!/ {next} {print}' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
          done

      if ! find "${TMPJS}" -type f \( -name '*.js' -o -name '*.jsx' \) -print0 \
          | xargs -0 code2flow --language js --source-type=module -o "${OUT}/cg_js.json" >/dev/null 2> "${OUT}/.js.err"; then
        echo "[warn] js失败: ${NAME}；看 ${OUT}/.js.err"
      fi
      rm -rf "${TMPJS}"
    else
      echo "[fallback] ${NAME} 无 esbuild 或转译失败，直接解析源并忽略语法错误"
      if ! xargs -0 code2flow --language js --source-type=module --skip-parse-errors \
           -o "${OUT}/cg_js.json" < "${JS_LIST}" >/dev/null 2> "${OUT}/.js.err"; then
        echo "[warn] js仍失败: ${NAME}；看 ${OUT}/.js.err"
      fi
    fi
  else
    echo "[skip js] ${NAME} 无 JS/TS"
  fi
  rm -f "${JS_LIST}"
done
