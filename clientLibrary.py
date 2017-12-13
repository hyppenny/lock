import json, requests

class clientLibrary():
    def filelist(self):
        request = requests.get("http://127.0.0.1:2333/test")
        filelist = json.loads(request.text)
        for f in filelist:
            print(f)

    def read(self):
        request = requests.get("http://127.0.0.1:2333/test")
        filename = json.loads(request.text)
