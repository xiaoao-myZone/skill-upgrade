# write
`wrnum = write(fd, buf, count)`
1. 部分写： count>wrnum， 磁盘被写满，或者进程资源的限制 RLIMIT_FSIZE
2. write成功并不能保证数据已写入磁盘， 因为因为内核为了提高效率会缓存磁盘的I/O操作