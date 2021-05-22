import os
import socket
import select
try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty

import traceback
import asyncio
SOCK_ADDR = ("127.0.0.1", 7002)

class SocketInterface(object):
    def __init__(self, system_manager, timeout=60):
        """
        Args:
            system_manager: instance of SystemManager child class
        """
        self.system_manager = system_manager
        self.timeout = timeout

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_addr = SOCK_ADDR
        self.server_socket.bind(server_addr)

        self.server_socket.listen(2)
        print("[Socket App] Server start, listen to {}:{}".format(*server_addr))
        self.server_socket.setblocking(False)

    
        self.epoll = select.epoll()
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN)

        self.msg_queues = {}

        self.fd_to_socket = {self.server_socket.fileno(): self.server_socket}
    
    @asyncio.coroutine
    def recv(self, sock_obj):
        return sock_obj.recv(1024)

    @asyncio.coroutine
    def run(self):
        while True:
            print("waiting for event")
            events = self.epoll.poll(self.timeout)
            if not events:
                continue
            for fd, event in events:
                socket = self.fd_to_socket[fd]
                if socket == self.server_socket:
                    connection, addr = self.server_socket.accept()
                    print("[Socket App] connection from {}:{}".format(*addr))
                    connection.setblocking(False)
                    self.epoll.register(connection.fileno(), select.EPOLLIN)
                    self.fd_to_socket[connection.fileno()] = connection
                    self.msg_queues[connection] = Queue()

                elif event & select.EPOLLHUP:
                    print("[Socket App] client close")
                    self.epoll.unregister(fd)
                    self.fd_to_socket[fd].close()
                    del self.fd_to_socket[fd]
                elif event & select.EPOLLIN:
                    #data = socket.recv(1024).decode()
                    data = yield from self.recv(socket)
                    data = data.decode()
                    if data:
                        print("[Socket App] accept {} from {}:{}".format(str(data), *socket.getpeername()))
                        self.msg_queues[socket].put(int(data))
                        self.epoll.modify(fd, select.EPOLLOUT)
                    else:
                        print("[Socket App] client close")
                        socket.close()
                        del self.fd_to_socket[fd]
                elif event & select.EPOLLOUT:
                    try:
                        msg = self.msg_queues[socket].get_nowait()
                    except Empty:
                        print("[Socket App] {}:{} queue empty".format(*socket.getpeername()))
                        self.epoll.modify(fd, select.EPOLLIN)
                    else:
                        try:
                            if msg == 1:#sock_cmd.START.value:
                                ret = yield from self.system_manager.start()
                            if msg == 2:
                                ret = "lalal"
                            #     print("[Socket App] call system manager %sING" % sock_cmd.START.name)
                            #     ret = self.system_manager.start()
                            # elif msg == sock_cmd.CONTINUE.value:
                            #     print("[Socket App] call system manager %sING" % sock_cmd.CONTINUE.name)
                            #     ret = self.system_manager.restart()
                            # elif msg == sock_cmd.PAUSE.value:
                            #     print("[Socket App] call system manager %sING" % sock_cmd.PAUSE.name)
                            #     ret = self.system_manager.cycle_stop()
                            # elif msg == sock_cmd.READ.value:
                            #     print("[Socket App] call system manager %sING" % sock_cmd.READ.name)
                            #     ret = self.system_manager.read()
                            # elif msg == sock_cmd.STOP.value:
                            #     print("[Socket App] call system manager %sING" % sock_cmd.STOP.name)
                            #     ret = self.system_manager.shutdown()
                        except:
                            #log.error("[Socket App] Error", exc_info=True)

                            traceback.print_exc()
                            #ret = sock_return.FAIL.value
                            ret = 1
                        socket.send((str(ret)).encode())
                        print("[Socket App] send return: {} to {}:{}".format(ret, *socket.getpeername()))


class SystemManager:
    @asyncio.coroutine
    def start(self):
        main_path = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])
        with open(os.path.join(main_path, "my_heap/ip.txt"), "r") as f:
            data = f.read()
        return data
si = SocketInterface(SystemManager())
task = asyncio.async(si.run())
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
