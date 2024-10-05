def log_info(ip_address: str, client: str, path: str, result: str):
    data = {"ip_address": ip_address, "client": client, "path": path, "result": result}
    print("Results", data)
