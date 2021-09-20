# Auto Start Script

[Ubuntu 下配置开机自启](https://blog.csdn.net/yu_xiaoxian_2018/article/details/105326417)
[详细](https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6)
[最详细](https://www.freedesktop.org/software/systemd/man/systemd.service.html#)


## step
1. build **.service in `/etc/systemd/system`
2. sudo systemctl daemon-reload
3. sudo systemctl start **.service
##  TODO
1. 如何保存输出流
2. 自动修改VPN