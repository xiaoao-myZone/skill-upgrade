1. 挂载磁盘分区(disk)
`sudo mount /dev/sdd1 /mnt` 
接着在/mnt中进行读写操作
2. 格式化磁盘
`sudo mkfs -t ntfs /dev/sdd1`
3. 解除挂载
`sudo umount /dev/sdd1`
需要在没有进程占用该磁盘的情况下

4. 创建磁盘分区
`sudo fdisk /dev/sdd`
接着输入n p w

5. 擦除签名
`sudo wipefs --all --force /dev/sdd`