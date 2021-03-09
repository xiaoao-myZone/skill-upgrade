from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_socketio import SocketIO
app = Flask("Demo")
api = Api(app)
ws = SocketIO(app)

@ws.on("connect")
def on():
    print("connected")

@ws.on("disconnect")
def dison():
    print("disconnected")

@app.route("/")
def index():
    return render_template("ws.html")
class Test(Resource):
    def get(self):
        return {"code": 0}

api.add_resource(Test, "/cmd")

#app.run(host="0.0.0.0", port=7005)
ws.run(app, host="0.0.0.0", port=7005)


