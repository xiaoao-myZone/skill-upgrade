# -*- coding: utf-8 -*-
import socketio
import time


# wiki地址：http://wiki.okjiaoyu.cn/pages/viewpage.action?spaceKey=RJBK&title=ailearn-instruction-svr
def func(token="", uid=0, room=0):
    sio = socketio.Client()
    event = 'my_event'

    @sio.event()
    def my_response(data):
        # handle the message
        # sio.emit('my_event', {"cmd": "joinRoom", "roomId": 8888})
        print(data)
        print(type(data))

    @sio.event
    def connect():
        print("I'm connected!")

    @sio.event
    def connect_error():
        print("The connection failed!")

    @sio.event
    def disconnect():
        print("I'm disconnected!")

    # url = 'http://ailearn-instruction-stress.xk12.cn:38999/?systemId={uid}&loginType=3&token={token}&userType=1'
    # dev环境的URL地址，端口38899
    # url = 'http://ailearn-instruction-dev.xk12.cn:38899/?systemId={uid}&loginType=3&token={token}&userType=1'
    url ="http://127.0.0.1:7002"
    # url = url.format(uid=uid, token=token)

    sio.connect(
        url,transports=["websocket"])
    print('my sid is', sio.sid)
    time.sleep(500)
    # 必需进行注册和加入room操作,room等于发布教学活动的activityid
    # sio.emit(event, {"cmd": "register", "userId": uid, "role": "T", "deviceVersion": "1.0","s_sid": sio.sid, "token": token})
    # sio.emit(event, {"cmd": "joinRoom", "roomId": room})
    time.sleep(3)

func()