import socket
import time

def check_tcp(target: str, port: int = 80, timeout: int = 3):
    start_time = time.time()
    try:
        with socket.create_connection((target, port), timeout=timeout):
            latency = round((time.time() - start_time) * 1000, 2)  # миллисекунды
            return {"status": "success", "latency_ms": latency, "port": port}
    except Exception as e:
        return {"status": "error", "error": str(e), "port": port}
