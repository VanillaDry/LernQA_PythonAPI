import requests
payload = {"name": "Vanilla"}
response = requests.get("https:playground.learnqa.ru/api/hello", params=payload)
print(response.text)