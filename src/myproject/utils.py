import requests

def greet(name: str) -> str:
    return f"Hello, {name}!"

def fetch_status(url: str) -> str:
    response = requests.get(url, timeout=5)
    return str(response.status_code)
