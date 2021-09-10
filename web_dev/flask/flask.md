## Falsk

1. with socketio
> &emsp; 直接在视图函数中调用socketio.emit没有问题,但是貌似只能发一次,多次发送最后直选最后一次,并且会干涉其他事件的通讯
> &emsp; 但是引入evenlet调用evenlet.monkey_patch()可以解决上述问题
> &emsp; 而gevent的monkey.patch_all()并不能解决这个问题
> &emsp; 将Queue, threading, socket提前导入,也不会影响性能
