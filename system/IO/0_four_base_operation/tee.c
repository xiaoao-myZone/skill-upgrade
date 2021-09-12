#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#define MAX_SIZE 20
char buffer[MAX_SIZE + 1];

void main(int argc, char *args[])
{   
    // printf("**********************"); // 这里的打印内容会随着第一次输出打印出来
    // TODO 为什么呢？
    int readnum = 0;
    while (1)
    {
        while (1)
        {
            
            readnum = read(STDIN_FILENO, buffer, MAX_SIZE);
            if ( readnum == -1) 
            {
                printf("error when read stdin\n");
                return;
            } else if ( readnum == 0) 
            {   
                // stdin末尾没有EOF， 所以代码正常情况不会进过这一段
                break;
            } else
            {
                buffer[readnum] = '\0';
                //如果在这里不做限制， 当上一次buffer写满
                // 这次就会把buffer上次未刷新的继续写出来
                printf("%s", buffer);
            }
            // else if (write(STDOUT_FILENO, buffer, readnum) != readnum)
            // {
            //     printf("error when write in stdout\n");
            // }
            
        }
    }
    
    
    
}