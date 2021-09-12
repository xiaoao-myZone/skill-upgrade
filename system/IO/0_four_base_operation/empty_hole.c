#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

void main(int argc, char *args[])
{
    off_t f_size;
    char buffer[6]="123456";
    if (argc <2)
    {
        printf("Please add file\n");
        return;
    }
    
    int fd = open(args[1], O_RDONLY);
    f_size = lseek(fd, 2, SEEK_END);
    printf("f_size is %d\n", (int)f_size);
    if (f_size==-1)
    {
        printf("error when lseek\n");
        return;
    }
    if (write(fd, buffer, 6)==-1)
    {
        printf("error when write\n");
        // TODO 不行失败了
        return;
    }

}