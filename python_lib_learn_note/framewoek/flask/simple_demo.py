from flask import Flask, render_template, request
from eventlet import monkey_patch; monkey_patch()

from flask_restful import Resource, Api
from flask_socketio import SocketIO
from types import FunctionType
import time
import logging as log
log.basicConfig(level=log.INFO)
log.info("hi")
app = Flask("Demo")
api = Api(app)
# ws = SocketIO(app, cors_allowed_origins="*", async_mode="threading")
ws = SocketIO(app)
#print(dir(api))

def GET_STD_RES(code=0, msg="success", data=True):
    if code == -1:
        res = {
            "code": code,
            "msg": "failed" if msg == "success" else msg,
            "data": False if isinstance(data, bool) else data
        }
    elif code == 0:
        res = {"code": code, "msg": msg, "data": data}
    else:
        raise Exception("undefined code num")

    return res
    
@ws.on("connect")
def on():
    print("connected")

@ws.on("disconnect")
def dison():
    print("disconnected")

@app.route("/")
def index():
    return render_template("ws.html")

def req_log(ignoreReq=False, ignoreRes=False):
    """Log all key messages of the request and resposne.

    Args:
        ignoreReq: bool, represents ignore request.data in log.
        ignoreRes: bool, represents ignore return data.
    """
    def _req_log(func):
        def _wrapper(*args, **kwargs):
            msg = "{} - {} - {} - {}".format(str(int(time.time()*1000)), request.remote_addr, request.path, request.method)
            if request.data:
                if ignoreReq:
                    msg_with_data = "{} - {}".format(msg, request.content_type)
                else:
                    msg_with_data = "{} - {}- {}".format(msg, request.content_type, request.data)
                log.info("request  - {}".format(msg_with_data))
            else:
                log.info("request  - {}".format(msg))

            try:
                ret = func(*args, **kwargs)
            except Exception as e:
                ret = GET_STD_RES(code=-1, msg="error", data=str(e))
                log.error("response - {} - {}".format(msg, str(ret)), exc_info=True)

            else:
                if ignoreRes:
                    log.info("response - {}".format(msg))
                else:
                    log.info("response - {} - {}".format(msg, str(ret)))
            return ret
        return _wrapper
    return _req_log
class Test(Resource):
    @req_log()
    def get(self):
        # for i in dir(request):
        #     if not i.startswith("_"):
        #         print("-"*20)
        #         print("attr: %s" % i)
        #         obj = getattr(request, i)
        #         print("type: %s" % type(obj))
        #         print("content: %s" % str(obj))
        #         print("-"*20)
        time.sleep(4)
        return {"code": 0}
    
    @req_log(ignoreReq=True, ignoreRes=False)
    def post(self):
        # for i in dir(request):
        #     if not i.startswith("_"):
        #         print("-"*20)
        #         print("attr: %s" % i)
        #         obj = getattr(request, i)
        #         print("type: %s" % type(obj))
        #         print("content: %s" % str(obj))
        #         print("-"*20)
        
        return {"code": 0}
    

api.add_resource(Test, "/cmd")
# for i in dir(api):
#     if not i.startswith("_"):
#         try:
#             print("-"*20)
#             print("attr: %s" % i)
#             obj = getattr(api, i)
#             print("type: %s" % type(obj))
#             print("content: %s" % str(obj))
#             print("-"*20)
#         except:
#             pass
#app.run(host="0.0.0.0", port=7005)
class Replace(Resource):
    def get(self):
        return {"code": -1}
    
    def post(self):
        data = request.json
        return {"code": -1, "data": data}

ws.run(app, host="0.0.0.0", port=7002, debug=False)


