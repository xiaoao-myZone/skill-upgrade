import socketio
def start_sio_client():
    index = "http://127.0.0.1:7002"

    # If reconnection is False, inner thread will terminate when the backend is closed
    socket_io = socketio.Client(reconnection=False)

    @socket_io.event
    def system_log(data):
        print("system_log")
        print(data)

    @socket_io.event
    def system_initialization(data):
        print("system_initialization")
        print(data)

    @socket_io.event
    def vision_node(data):
        print("vision_node")
        print(data)

    @socket_io.event
    def node_error(data):
        print("node_error")
        print(data)

    # connect will open a non-deamon thread to listen events
    socket_io.connect(index)#, transports=["websocket"])
    # 当后端使用eventlet时， 添加参数transports=["websocket"]
    # 当后端使用SocketIO(app, cors_allowed_origins="*", async_mode="threading")时， 


start_sio_client()
