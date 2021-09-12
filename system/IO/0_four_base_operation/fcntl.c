#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

// 使用 fcntl 函数 获取，设置文件的状态标志 https://www.cnblogs.com/scut-fm/p/3375177.html
void main(int argc, char *args[]){
    int val;
    if (argc < 2) {
        printf("Usage ./test 1\n");
        return;
    }
        
    val = fcntl(atoi(args[1]), F_GETFL, 0);
    if (val<0) {
        printf("error: %d\n", val);
        return;
    }
    switch (val & O_ACCMODE)
    {
    case O_RDONLY:
        printf("read only\n");
        break;
    case O_WRONLY:
        printf("write only\n");
        break;
    case O_RDWR:
        printf("read and write\n");
        break;
    default:
        printf("Unknown access mode: %d\n", val & O_ACCMODE);
        return;
    }
    if (val & O_APPEND)
        printf("append\n");
    if (val & O_ASYNC)
        printf("async\n");
    if (val & O_NONBLOCK)
        printf("no block\n");
    if (val & O_DSYNC)
        printf("dsync\n");
    if (val & O_SYNC)
        printf("sync\n");
}


