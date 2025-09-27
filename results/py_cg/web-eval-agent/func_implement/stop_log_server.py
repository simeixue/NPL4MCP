# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/utils.py
# module: webEvalAgent.src.utils
# qname: webEvalAgent.src.utils.stop_log_server
# lines: 4-20
def stop_log_server():
     """Stop the log server on port 5009.
     
     This function attempts to stop any process running on port 5009
     by killing the process if it's a Unix-like system, or using taskkill
     on Windows.
     """
     try:
         if platform.system() == "Windows":
             subprocess.run(["taskkill", "/F", "/PID", 
                             subprocess.check_output(["netstat", "-ano", "|", "findstr", ":5009"]).decode().strip().split()[-1]], 
                             stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
         else:  # Unix-like systems (Linux, macOS)
             subprocess.run("kill $(lsof -ti tcp:5009)", shell=True, 
                             stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
     except Exception:
         pass  # Ignore errors if no process is running on that port