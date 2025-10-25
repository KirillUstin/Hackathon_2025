import socket

def check_dns(host: str) -> dict:
    try:
        ip = socket.gethostbyname(host)
        return {"status": "success", "ip": ip}
    except Exception as e:
        return {"status": "error", "error": str(e)}
