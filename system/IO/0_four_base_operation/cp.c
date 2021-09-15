#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#define MAX_SIZE 20
/*
带空洞的文件copy后无法在vscode中正常显示，然后我把文件后面的空洞删掉
接着运行制造空洞的文件， 接着再拷贝， 可以了
我猜是因为之前没有加close
问题是： \0是什么时候加上去的? 没人加上去，除非自己写上去
\0是不是就是0?是
*/
void print(int len, char * string)
{
    printf("%d", '\0'==0);
    for (int i = 0; i<len; i++)
    {
        if ((*string) == 0)  //空洞的值确实是0，并且%c打印不出来
        {
            printf("~");
        } else if ((*string) == '\0')
        {
            printf("+");
        }
        printf("%c", *string++); // * 运算优先级小于++
    }
}

void main(int argc, char *args[])
{
    char buffer[MAX_SIZE+1];
    int fd = -1, t_fd = -1, readnum = -1, numWritten = -1;
    if (argc < 3)
    {
        printf("Please add two file like cp\n");
        return;
    }
    fd = open(args[1], O_RDONLY);
    if (fd==-1)
    {
        printf("error when open %s\n", args[1]);
        return;
    }
    t_fd = open(args[2], O_CREAT | O_WRONLY | O_TRUNC, 
                S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH);
    if (t_fd==-1)
    {
        printf("error when open %s\n", args[2]);
        return;
    }
    while (1)
    {
        readnum = read(fd, buffer, MAX_SIZE);
        buffer[readnum] == '\0';
        print(readnum, buffer);
        numWritten = write(t_fd, buffer, readnum);
        if (numWritten != readnum)
        {
            printf("error when write\n");
            return;
        }
        // printf("%s", buffer);// 注意%s会自动在遇到\0时停止打印
        if (readnum<MAX_SIZE)
            break;

    }
    if (close(fd)==-1)
    {
        printf("error when close source\n");
        return;
    }
    if (close(t_fd)==-1)
    {
        printf("error when close target\n");
        return;
    }
    printf("success\n");

}