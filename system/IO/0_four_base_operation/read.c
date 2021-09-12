#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#define MAX_READ 20
#define STDIN_FILENO 0
char buffer[MAX_READ];


void main(){
    if (read(STDIN_FILENO, buffer, MAX_READ) == -1)
        printf("read failed");
    else
        // buffer[2] = '\n'; // \n并不能作为%s的结束标志
        printf("The input data was: %s\n", buffer);
        // 如果输入的长度大于MAX_READ，该程序会截取前MAX_READ个字符输出
        // 同时， 将剩余的字符作为后面的shell命令， 这意味者shell背后一直有一个进程阻塞早在从stdin里读取string，遇到\n结束阻塞

}