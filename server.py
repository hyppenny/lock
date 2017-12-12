from flask import Flask
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        #return "Connecting"
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
        request.add_argument('post', type = str, location = 'json')
        print(request.parse_args()['post'])

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(port = 2333)
