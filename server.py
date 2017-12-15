from flask import Flask
from flask_restful import Api, Resource, reqparse
import os, shutil

app = Flask(__name__)
api = Api(app)


class fileList(Resource):
    def get(self):
        # return "Connecting"
        # files = []
        # file_path = os.path.dirname(os.path.realpath(__file__)) + "/example"
        # print(file_path)
        #
        # for filename in os.listdir(file_path):
        #     print(filename)
        #     files.append(filename)
        # print(files)
        updateList()
        return filelist

    def post(self):
        request = reqparse.RequestParser()
        request.add_argument('filename', type=str, location='json')
        request.add_argument('content', type=str, location='json')

        print(request.parse_args()['filename'], "to add")
        filename = request.parse_args()['filename']
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        f = [f for f in filelist if f == filename]
        if len(f)!= 0:
            return False
        #filelist.append(filename)
        updateList()
        addPath = os.path.join(file_path, filename)
        addFile = open(addPath, 'w')
        addFile.write(request.parse_args()['content'])
        addFile.close()
        with open(os.path.join(file_path, filename)) as f:
            data = f.readlines()
        return data



class fileItself(Resource):
    def get(self, filename):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        #print(os.path.join(file_path, f))
        file = ''
        for f1 in filelist:
            if f1 == filename:
                file = f1
        # print(file)
        if len(file) == 0:
            return False
        with open(os.path.join(file_path, file)) as f:
            data = f.readlines()
        return data

    def put(self, filename):
        request = reqparse.RequestParser()
        request.add_argument('content', type=str, location='json')
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        f = [f for f in filelist if f == filename]
        if len(f) == 0:
            return False
        editPath = os.path.join(file_path, filename)
        currentFile = open(editPath, 'w')
        currentFile.write(request.parse_args()['content'])
        currentFile.close()
        with open(os.path.join(file_path, filename)) as f:
            content = f.readlines()
        return content

    def delete(self, filename):
        print("111")
        file_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        f = [f for f in filelist if f == filename]
        if len(f) == 0:
            return False
        deletePath = os.path.join(file_path, filename)
        # print(filelist,"@@@")
        os.remove(deletePath)
        # print(filelist,"!!!")
        #filelist.remove(filename)
        # print(filelist,"###")
        #print('222')
        updateList()
        print(filelist)
        return True

class folder(Resource):
    def get(self):
        return dirlist

    def post(self):
        request = reqparse.RequestParser()
        request.add_argument('folder', type=str, location='json')
        newdir = request.parse_args()['folder']
        # print(request.parse_args(),newdir,"@@@@")
        d = [d for d in dirlist if d == newdir]
        if len(d) != 0:
            return False
        os.makedirs(os.path.join(file_path, newdir))
        #dirlist.append(newdir)
        updateList()
        return True

    def put(self):
        request = reqparse.RequestParser()
        request.add_argument('filename', type=str, location='json')
        request.add_argument('newName', type=str, location='json')
        filename = request.parse_args()['filename']
        newName = request.parse_args()['newName']
        d = [d for d in dirlist if d == filename]
        if len(d) == 0:
            return False
        os.rename(os.path.join(file_path,filename),os.path.join(file_path, newName))
        # dirlist.remove(filename)
        # dirlist.append(newName)
        updateList()
        return True

    def delete(self):
        request = reqparse.RequestParser()
        request.add_argument('folder', type=str, location='json')
        dir = request.parse_args()['folder']
        d= [d for d in dirlist if d ==dir]
        if len(d) == 0:
            return False
        shutil.rmtree(os.path.join(file_path, dir))
        updateList()

        return True





api.add_resource(fileList, '/fileList')
api.add_resource(fileItself, '/file/<string:filename>')
api.add_resource(folder, '/folder')

def updateList():

    #print(file_path)
    del dirlist[:]
    del filelist[:]
    for dir, subDir, fileList in os.walk(file_path):
        print('Directory: {}'.format(dir[dir.rfind(file_path) + len(file_path) + 1:]))
        dirlist.append(dir[dir.rfind(file_path) + len(file_path) + 1:])
        for f in fileList:
            print(f)
            filelist.append(os.path.join(dir, f)[os.path.join(file_path, f).rfind(dir_path) + len(dir_path) + 1:])


if __name__ == '__main__':
    dirlist = []
    filelist = []
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/example"
    dir_path = os.path.dirname(os.path.realpath(__file__))+ "/example"
    app.run(port=2333)
