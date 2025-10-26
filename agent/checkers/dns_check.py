import dns.resolver

def check_dns(target: str):
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    results = {}

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(target, rtype)
            results[rtype] = [str(rdata) for rdata in answers]
        except dns.resolver.NoAnswer:
            results[rtype] = []
        except Exception as e:
            results[rtype] = {"error": str(e)}

    return {"status": "success", "records": results}
