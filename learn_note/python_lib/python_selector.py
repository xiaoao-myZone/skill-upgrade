import socket
import selectors
import traceback

selector = selectors.PollSelector
"""
with _ServerSelector() as selector:
    selector.register(self, selectors.EVENT_READ)
    ready = selector.select(poll_interval)
"""
# with selector() as slt:
    # print(dir(slt))
"""
['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', 
'_abc_negative_cache_version', '_abc_registry', '_fd_to_key', '_fileobj_lookup', 
'_key_from_fd', '_map', '_poll', 'close', 'get_key', 'get_map', 'modify', 'register', 
'select', 'unregister']
"""


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1", 7006))
server.listen(5)
server.setblocking(False)

s_fd = server.fileno()

with selector() as epoll:
    epoll.register(s_fd, selectors.EVENT_READ)
    try:
        while True:
            events = epoll.select(2)
            print(ret)
            for selectkey in events:
                if selectkey.fileno() == s_fd:
                    conn, addr = server.accept()
                    epoll.register(conn, selectors.EVENT_WRITE)
                elif selectkey.fileno()
                    pass
    except:
        traceback.print_exc()
