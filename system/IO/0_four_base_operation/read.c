#include <stdio.h>
#include <fcntl.h>
#define MAX_READ 20
#define STDIN_FILENO 0
char buffer[MAX_READ];


void main(){
    if (read(STDIN_FILENO, buffer, MAX_READ) == -1)
        printf("read failed");
    else
        printf("The input data was: %s\n", buffer);

}