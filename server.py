from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


class test(Resource):
    def get(self):
        return "Connecting"

    def post(self):
        request = reqparse.RequestParser()
        request.add_argument('post', type = str, location = 'json')
        print(request.parse_args()['post'])

api.add_resource(test, '/test')

if __name__ == '__main__':
    app.run(port = 2333)