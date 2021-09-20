# USB disable problem

## 问题描述
1. 在通电情况下， usb可以做到恢复了（不知道是不是下载laptop_mode_tools和tlp有卸载造成的）
2. 在电池供电情况下， usb无法立刻恢复， 不知道是要等一会还是因为AC电源接上的原因
3. 有的接口实现上述状态可以， 有的不可以， 应该是USB2.0与3.0的区别造成的

## 方案
1. [USB ports not working after resume from sleep on Ubuntu 18.04](https://askubuntu.com/questions/1044988/usb-ports-not-working-after-resume-from-sleep-on-ubuntu-18-04)
其中第一种方法推荐编辑`/etc/default/grub`中改为`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash usbcore.autosuspend=-1"`, 然后`sudo update-grub`，重启。第二种方案是在`/lib/systemd/system-sleep`添加shell脚本，每次开机后恢复USB

2. 使用laptop_mode[https://zhidao.baidu.com/question/504437678.html](https://zhidao.baidu.com/question/504437678.html)
但是应用了laptop_mode后， 笔记本风扇一直在转， 这怎么可能省电？

3. 使用tlp

## 总结
1. 根据`/etc/systemd/logind.conf`中的默认配置， 在通电情况下`HandleLidSwitchExternalPower=suspend`是采用suspend模式， 在不通电情况下`HandleLidSwitch=hibernate`采用hibernate模式
2. 在`/lib/systemd/system-sleep`添加一个执行写入hello world到txt的脚本， 发现无论是在通电情况下合盖/开盖，还是不通电， 都会有两个hello world， 应该根据case $1 in pre/post)来区分， 所以系统确实尝试恢复USB功能， 并且应该是通过这个下的脚本`hdparm`来实现的，执行的命令为`/usr/lib/pm-utils/power.d/95hdparm-apm resume`

3. 根据`/lib/systemd/system-sleep`中的脚本的写法， 可知， 在合盖与开盖的时候， 会调用里面的每个sh脚本， 并且加上参数 script suspend/hibernate/hybrid-sleep pre/post

4. `/usr/lib/pm-utils/power.d/`中存在usb_bluetooth



## usb shell
1. lsusb
2. lspci | grep USB
## Referrence
1. [laptop_mode](https://blog.csdn.net/iteye_16723/article/details/81615444)
2. [如何從命令行重置USB設備？](https://ubuntuqa.com/zh-tw/article/409.html)
3. [ubuntu doc for logind.config](http://manpages.ubuntu.com/manpages/trusty/man5/logind.conf.5.html)
4. [tlp 官方文档](https://linrunner.de/tlp/#installation)