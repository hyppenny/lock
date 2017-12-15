import json, requests
from clientLibrary import clientLibrary

if __name__ == "__main__":
    while True:
        option = int (input("\nPlease input a number from menu:\n1.View file\n2.Read file\n3.Edit file\n4.Add file\n5.Delete file\n6.View folder\n7.Add folder\n8.Rename folder\n9.Delete folder\n0.Exit\n"))
        if option == 1:
            clientLibrary.filelist(clientLibrary)

        elif option == 2:
            clientLibrary.filelist(clientLibrary)
            f = input("Please input the file you want to read: ")
            clientLibrary.read(clientLibrary, f)

        elif option == 3:
            clientLibrary.filelist(clientLibrary)
            f = input("Please input the file name you want to edit:")
            if clientLibrary.lockFile(clientLibrary, "127.0.0.1:2333", f) != False:
                content = input("Please input the new content:")
                clientLibrary.edit(clientLibrary, f, content)
                clientLibrary.unlockFile(clientLibrary, "127.0.0.1:2333", f)
            else:
                print("File occupied")

        elif option == 4:
            f = input("Please input the name of the file you want to add: ")
            content  = input("Please input the content of your file:")
            clientLibrary.add(clientLibrary, f, content)

        elif option == 5:
            clientLibrary.filelist(clientLibrary)
            f = input("Please input the file you want to delete:")
            clientLibrary.delete(clientLibrary, f)

        elif option == 6:
            clientLibrary.folder(clientLibrary, "127.0.0.1:2333")


        elif option == 7:
            f = input("Please input the name of your new folder:")
            clientLibrary.addFolder(clientLibrary, "127.0.0.1:2333", f)

        elif option == 8:
            filename = input("Please input the folder you want to rename:")
            newName = input("Please input the new name:")
            clientLibrary.renameFolder(clientLibrary, "127.0.0.1:2333", filename, newName)


        elif option == 9:
            f = input("Please input the folder you want to delete: ")
            clientLibrary.deleteFolder(clientLibrary, "127.0.0.1:2333",f)


        elif option == 0:
            break

        input()