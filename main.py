import subprocess
import sys
from pathlib import Path

YELLOW = "\033[93m"
RESET = "\033[0m"

def run_cmd(name: str, cmd: str) -> bool:
    print(f"[RUN] {name}: {cmd}")
    proc = subprocess.run(cmd, shell=True)
    if proc.returncode != 0:
        print(f"[FAIL] {name} 执行失败 (exit {proc.returncode})")
        return False
    return True

def check_pycg_results(base: Path) -> bool:
    ok = True
    for proj_dir in base.iterdir():
        cg = proj_dir / "cg_py.json"
        if not cg.exists() or cg.stat().st_size == 0:
            print(f"{YELLOW}{proj_dir.name}不能生成call graph{RESET}")
            ok = False
    return ok

def check_func_results(base: Path) -> bool:
    ok = True
    for proj_dir in base.iterdir():
        func_dir = proj_dir / "func_implement"
        if not func_dir.exists() or not any(func_dir.glob("*.py")):
            print(f"{YELLOW}{proj_dir.name}不能生成func_implement{RESET}")
            ok = False
    return ok

if __name__ == "__main__":
    pycg_dir = Path("./results/py_cg")

    # Step 1: pycg
    if not run_cmd("pycg", "sh ./gen_cg/pycg.sh"):
        sys.exit(1)
    check_pycg_results(pycg_dir)

    # Step 2: extract_funcs
    if not run_cmd("extract_funcs", "sh ./gen_cg/extract_funcs.sh"):
        sys.exit(1)
    check_func_results(pycg_dir)

    # Step 3: get_tool_list
    if not run_cmd("get_tool_list", "python ./get_tool_list.py"):
        print("server启动失败")
        sys.exit(1)

    # Step 4: get_implementation (只在前面都成功的情况下执行)
    if not run_cmd("get_implementation", "python ./get_implementation.py"):
        sys.exit(1)

    print("[DONE] 全部步骤执行完毕")
