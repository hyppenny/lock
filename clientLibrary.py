import json, requests


class clientLibrary():
    def filelist(self):
        request = requests.get("http://127.0.0.1:2333/fileList")
        filelist = json.loads(request.text)
        for f in filelist:
            print(f)

    def read(self, f):
        request = requests.get("http://127.0.0.1:2333/file/{}".format(f))
        content = json.loads(request.text)
        if content is False:
            print("File does not exist")
        else:
            for c in content:
                print(c, end='')

    def add(self, filename, content):
        request = requests.post("http://127.0.0.1:2333/fileList", json = {'filename': filename, 'content':content})
        content = json.loads(request.text)
        if content is False:
            print("File existed already")
        else:
            for c in content:
                print(c, end='')
            print("File has been added successfully")

    def edit(self, filename, content):
        request = requests.put("http://127.0.0.1:2333/file/{}".format(filename), json= {'content': content})
        #print("")
        content = json.loads(request.text)
        if content is False:
            print("File does not exist")#???
        else:
            for c in content:
                print(c, end='')
            print("\nFile has been changed")

    def delete(self, filename):
        request = requests.delete("http://127.0.0.1:2333/file/{}".format(filename))
        #print(request.text)
        content = json.loads(request.text)
        if content is False:
            print("File does not exist")
        else:
            print("File deleted")#???

    def folder(self, path):
        request = requests.get("http://{path}/folder".format(path))
        foldername = json.loads(request.text)
        print("Folder:")
        for f in foldername:
            print(f)

    def addFolder(self, path, foldername):
        request = requests.post("http://{}/folder".format(path), json={'foldername':foldername})
        content = json.loads(request.text)
        if content:
            print("Folder added")
        else:
            print("Folder already exist")