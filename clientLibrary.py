import json, requests


class clientLibrary():
    def filelist(self):
        request = requests.get("http://127.0.0.1:2333/fileList")
        filelist = json.loads(request.text)
        for f in filelist:
            print(f)

    def read(self, f):
        request = requests.get("http://127.0.0.1:2333/file/{}".format(f))
        data = json.loads(request.text)
        for d in data:
            print(d, end='')
