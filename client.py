import json, requests
from clientLibrary import clientLibrary

if __name__ == "__main__":
    option = int (input("Please input a number from menu:\n1.View file\n2.Read file\n3.Edit file\n4.Add file\n5.Delete file\n"))
    if option == 1:
        clientLibrary.filelist(clientLibrary)

    if option == 2:
        clientLibrary.filelist(clientLibrary)
        f = input("Please input thr file you want to read:")
        clientLibrary.filelist(f)


    '''if option == 3:

    if option == 4:

    if option == 5:'''

request = requests.post("http://127.0.0.1:2333/test", json={'post': "Connected"})