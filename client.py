import json, requests

request = requests.get("http://127.0.0.1:2333/test")
print(json.loads(request.text))
request = requests.post("http://127.0.0.1:2333/test", json = {'post': "Connected"})