from flask import Flask
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)


class fileList(Resource):
    def get(self):
        # return "Connecting"
        files = []
        file_path = os.path.dirname(os.path.realpath(__file__)) + "/example"
        print(file_path)

        for filename in os.listdir(file_path):
            print(filename)
            files.append(filename)
        print(files)
        return files

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
        filelist.append(filename)
        addPath = os.path.join(file_path, filename)
        addFile = open(addPath, 'w')
        addFile.write(request.parse_args()['content'])
        addFile.close()
        with open(os.path.join(file_path, f)) as f:
            data = f.readlines()
        return data



class fileItself(Resource):
    def get(self, f):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        print(os.path.join(file_path, f))
        file = ''
        for f1 in filelist:
            if f1 == f:
                file = f1
        # print(file)
        if len(file) == 0:
            return False
        with open(os.path.join(file_path, f)) as f:
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
        #print("111")
        file_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        f = [f for f in filelist if f == filename]
        if len(f) == 0:
            return False
        deletePath = os.path.join(file_path, filename)
        os.remove(deletePath)
        filelist.remove(filelist.index(filename))
        #print('222')
        print(filelist)
        return True


api.add_resource(fileList, '/fileList')
api.add_resource(fileItself, '/file/<string:f>')

if __name__ == '__main__':
    filelist = []
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/example"
    for filename in os.listdir(file_path):
        print(filename)
        filelist.append(filename)
    '''content = open(os.path.join(file_path, "file1.txt")).readlines()
    for c in content:
        print(c, end='')'''
    app.run(port=2333)
