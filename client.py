import json, requests

if __name__ == "__main__":
    option = int (input("Please input a number from menu:\n1.View file\n2.Read file\n3.Edit file\n4.Add file\n5.Delete file\n"))
    if option == 1:
        request = requests.get("http://127.0.0.1:2333/test")
        filelist = json.loads(request.text)
    for f in filelist:
        print(f)

request = requests.post("http://127.0.0.1:2333/test", json={'post': "Connected"})