import platform
import subprocess

def check_ping(host: str) -> dict:
    param = "-n" if platform.system().lower()=="windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            capture_output=True,
            text=True
        )
        success = result.returncode == 0
        return {"status": "success" if success else "fail", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}
