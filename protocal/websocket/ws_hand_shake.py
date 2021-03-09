# 1
"""
GET /socket.io/?EIO=2&transport=polling&t=1615123712979-153 HTTP/1.1

Host: 127.0.0.1:7005
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://127.0.0.1:7005/
Cookie: io=e58083a87bb44ae1be8e81b08443edf4
"""

[
    'HTTP/1.1 200 OK\r\n',
    'Set-Cookie: io=fa8b43a011f443de928212d4c6050c86; path=/; SameSite=Lax\r\n',
    'Content-Type: application/octet-stream\r\n',
    'Access-Control-Allow-Credentials: true\r\n', 
    'Content-Length: 119\r\n',
    'Date: Sun, 07 Mar 2021 13:28:32 GMT\r\n', 
    'Connection: keep-alive\r\n',
    '\r\n',
    '\x00\x01\x00\t\xff0{"pingInterval":25000,"pingTimeout":60000,"upgrades":["websocket"],"sid":"fa8b43a011f443de928212d4c6050c86"}\x00\x02\xff40'
]
# TODO understand the \x code, it must have assciation with struct

# 2
"""
POST /socket.io/?EIO=2&transport=polling&t=1615123712990-154&sid=fa8b43a011f443de928212d4c6050c86 HTTP/1.1

Host: 127.0.0.1:7005
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-type: application/octet-stream
Content-Length: 10
Origin: http://127.0.0.1:7005
Connection: keep-alive
Referer: http://127.0.0.1:7005/
Cookie: io=fa8b43a011f443de928212d4c6050c86

/u0y40/test TODO make sure
"""
[
    'HTTP/1.1 200 OK\r\n', 'Content-Type: text/plain\r\n',
    'Access-Control-Allow-Origin: http://127.0.0.1:7005\r\n',
    'Access-Control-Allow-Credentials: true\r\n', 
    'Content-Length: 2\r\n',
    'Date: Sun, 07 Mar 2021 13:28:32 GMT\r\n', 
    'Connection: keep-alive\r\n',
    '\r\n', 'OK'
]

# 3
"""
GET /socket.io/?EIO=2&transport=polling&t=1615123712997-155&sid=fa8b43a011f443de928212d4c6050c86 HTTP/1.1

Host: 127.0.0.1:7005
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://127.0.0.1:7005/
Cookie: io=fa8b43a011f443de928212d4c6050c86
"""

[
    'HTTP/1.1 200 OK\r\n', 'Content-Type: application/octet-stream\r\n',
    'Access-Control-Allow-Credentials: true\r\n', 'Content-Length: 68\r\n',
    'Date: Sun, 07 Mar 2021 13:28:33 GMT\r\n', 'Connection: keep-alive\r\n',
    '\r\n',
    '\x00\x05\x04\xff42/test,["my response",{"count":0,"data":"Connected"}]\x00\x07\xff40/test'
]

# 4

"""
GET /socket.io/?EIO=2&transport=websocket&sid=fa8b43a011f443de928212d4c6050c86 HTTP/1.1

Host: 127.0.0.1:7005
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Sec-WebSocket-Version: 13
Origin: http://127.0.0.1:7005
Sec-WebSocket-Extensions: permessage-deflate
Sec-WebSocket-Key: ZBiN1e2b8dzPg0S4TuDxLA==
Connection: keep-alive, Upgrade
Cookie: io=fa8b43a011f443de928212d4c6050c86
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket
"""

"""
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: Ri73H3VYXFsmz/pgFO47SvhEbp8=
Sec-WebSocket-Extensions: permessage-deflate
"""

"""
POST /socket.io/?EIO=2&transport=polling&t=1615123713016-156&sid=fa8b43a011f443de928212d4c6050c86 HTTP/1.1

Host: 127.0.0.1:7005
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-type: application/octet-stream
Content-Length: 50
Origin: http://127.0.0.1:7005
Connection: keep-alive
Referer: http://127.0.0.1:7005/
Cookie: io=fa8b43a011f443de928212d4c6050c86
"""
#I'm connected!
[
    'HTTP/1.1 200 OK\r\n', 'Content-Type: text/plain\r\n',
    'Access-Control-Allow-Origin: http://127.0.0.1:7005\r\n',
    'Access-Control-Allow-Credentials: true\r\n', 'Content-Length: 2\r\n',
    'Date: Sun, 07 Mar 2021 13:28:33 GMT\r\n', 'Connection: keep-alive\r\n',
    '\r\n', 'OK'
]

# 5
"""
GET /socket.io/?EIO=2&transport=polling&t=1615123713021-157&sid=fa8b43a011f443de928212d4c6050c86 HTTP/1.1

Host: 127.0.0.1:7005
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://127.0.0.1:7005/
Cookie: io=fa8b43a011f443de928212d4c6050c86
"""

[
    'HTTP/1.1 200 OK\r\n', 'Content-Type: application/octet-stream\r\n',
    'Access-Control-Allow-Credentials: true\r\n', 'Content-Length: 4\r\n',
    'Date: Sun, 07 Mar 2021 13:28:33 GMT\r\n', 'Connection: keep-alive\r\n',
    '\r\n', '\x00\x01\xff6'
]
