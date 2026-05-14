import requests

data = {
    "app_name": "chrome",
    "url": "leetcode.com/problems/two-sum"
}

try:
    response = requests.post("http://localhost:5000/classify", json=data)
    print(response.json())
except Exception as e:
    print(f"Error: {e}")