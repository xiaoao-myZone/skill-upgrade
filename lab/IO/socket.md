## socket

1. 如果一对socket对象中， 一方的send已经调用结束， 而另一方的recv还在等待， 则接受方会报错socket.error: [Errno 11] Resource temporarily unavailable
2. 照理说不应该出现这种情况