"""
https://www.cnpython.com/qa/156358
https://stackoverflow.com/questions/53356451/pyzmq-high-water-mark-not-working-on-pub-socket/53360536#53360536
http://api.zeromq.org/
http://api.zeromq.org/master:zmq-setsockopt
"""
import zmq
import sys
import select

def get_event_list():
    events = []
    for event in dir(select):
        if event.startswith("EPOLL") and "_" not in event:
            events.append(event)
    events.sort(key=lambda x: getattr(select, x))
    return events[:-2]

event_list = get_event_list()

def map_event(num):
    global event_list
    bin_splits = list(bin(num)[2:])
    bin_splits.reverse()
    for index, No in enumerate(bin_splits):
        if No == '1':
            try:
                event = event_list[index]
                print(event, end=" ")
            except IndexError:
                print("Unknwon event", end= " ")
    print("\n")

def subscribe(url, sub):

    ctx = zmq.Context()
    client = ctx.socket(zmq.SUB)
    client.setsockopt(zmq.RCVHWM, 1)
    client.setsockopt(zmq.RCVBUF, 1)
    for prefix in sub:
        client.setsockopt(zmq.SUBSCRIBE, prefix.encode())
    if not sub:
        client.setsockopt(zmq.SUBSCRIBE, "".encode())
    
    client.connect(url)
    epoll = select.epoll()
    client_fd = client.fileno()
    epoll.register(client_fd)
    while True:
        events = epoll.poll(40)
        if events:
            print(events)
        for fd, event in events:
            map_event(event)
            if fd==client_fd:
                if event & select.EPOLLIN:
                    epoll.modify(fd, select.EPOLLOUT) # EPOLLOUT与EPOLLIN的含义与socket相反
                elif event & select.EPOLLOUT:
                    data = client.recv_string()
                    print(data)
                    


if __name__ == "__main__":
    url = sys.argv[1]
    sub = sys.argv[2:]
    print("sub: %s" % str(sub))
    print("subscribe...")
    subscribe(url, sub)


