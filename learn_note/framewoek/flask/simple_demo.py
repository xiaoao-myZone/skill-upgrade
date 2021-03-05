from flask import Flask
from flask_restful import Resource, Api
app = Flask("Demo")
api = Api(app)

class Test(Resource):
    def get(self):
        return {"code": 0}

api.add_resource(Test, "/")

app.run(host="0.0.0.0", port=7005)


