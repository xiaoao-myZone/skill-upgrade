# logical  https://blog.csdn.net/m0_38061194/article/details/79295773
# query api 
from app import app, socketio


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='7002', debug=app.config['DEBUG'])