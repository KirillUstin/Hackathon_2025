import subprocess

def check_traceroute(target: str) -> dict:
    try:
        cmd = ["tracert", "-d", "-w", "1000", target]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        output = result.stdout.strip().splitlines()

        hops = []
        for line in output:
            if line.strip().startswith("1") or line.strip()[0].isdigit():
                parts = line.split()

                try:
                    hop_number = int(parts[0])
                    ip = parts[-1]
                    
                    times = [float(p.replace("ms", "")) for p in parts if "ms" in p]
                    avg_time = sum(times) / len(times) if times else None

                    hops.append({
                        "hop": hop_number,
                        "ip": ip,
                        "time_ms": avg_time
                    })
                except Exception:
                    continue

        return {
            "status": "ok",
            "target": target,
            "hops": hops,
            "hop_count": len(hops)
        }

    except subprocess.TimeoutExpired:
        return {"status": "error", "error": "Traceroute timed out"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
