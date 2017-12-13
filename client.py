import json, requests
from clientLibrary import clientLibrary

if __name__ == "__main__":
    while True:
        option = int (input("\nPlease input a number from menu:\n1.View file\n2.Read file\n3.Edit file\n4.Add file\n5.Delete file\n6.Exit\n"))
        if option == 1:
            clientLibrary.filelist(clientLibrary)

        elif option == 2:
            clientLibrary.filelist(clientLibrary)
            f = input("Please input the file you want to read: ")
            clientLibrary.read(clientLibrary, f)

        elif option == 3:
            clientLibrary.filelist(clientLibrary)
            f = input("Please input the file name you want to edit:")
            content = input("Please input the new content:")
            clientLibrary.edit(clientLibrary, f, content)
        elif option == 4:
            f = input("Please input the name of the file you want to add: ")
            content  = input("Please input the content of your file:")
            clientLibrary.add(clientLibrary, f, content)

        elif option == 5:
            pass

        elif option == 6:
            pass
request = requests.post("http://127.0.0.1:2333/test", json={'post': "Connected"})