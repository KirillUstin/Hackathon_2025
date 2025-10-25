import requests

def check_http(url: str) -> dict:
    try:
        r = requests.get(url, timeout=5)
        return {
            "status": "success" if r.status_code == 200 else "fail",
            "status_code": r.status_code,
            "text_snippet": r.text[:100]
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
