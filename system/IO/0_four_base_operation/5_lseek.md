# lseek
`success = lseek(fd, offset, whence)`
1. 读写偏移量或者指针，单位是字节
2. 文件打开时，为0
3. 随着读或写， 会自动偏移
4. args: offset, 相对偏移量； whence, 绝对偏移量, SEEK_SET(初始位置), SEEK_CUR(当前位置), SEEK_END(文件尾部)
5. return: 成功，返回当前绝对偏移量？失败，返回-1
6. lseek并没有引起任何物理设备的访问与改动
6. 问题：
* 成功后返回的偏移量是以哪个位置为基准？
* offset参数可否为负数？如果可以为负数， 移动后的绝对偏移量小于0会如何？
* whence=SEEK_END， offset=n， 那么新增的n-1个没有写入的字符位的值是多少？ 这叫做文件空洞， read会返回0(缓冲区的值是不是都是0？)， write时会把之前的offset以0的方式写入（待验证o9）