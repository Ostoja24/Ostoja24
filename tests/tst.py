import requests

dataset = "global"
r = requests.get(f"https://api.coinlore.net/api/{dataset}",
                 headers=None,
                 auth=None,
                 params=None)
print(r.content)
print(r.json())