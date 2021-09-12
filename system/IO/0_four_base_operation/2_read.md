1. 为什么在C语言中调用ead(STDIN_FILENO, buffer, MAX_READ)会被阻塞？
* 这大概是因为STDIN_FILENO的文件打开方式采用了O_ASYNC?