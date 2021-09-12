# read

1. 为什么在C语言中调用ead(STDIN_FILENO, buffer, MAX_READ)会被阻塞？
* 这大概是因为STDIN_FILENO的文件打开方式采用了O_ASYNC?不是
* 凭什么read的时候， 当文件中没有数据时会被阻塞？还是说， read设计之初就是这么定义的
* 但是书中说道，只有在遇到EOF或者数目达标后， read才返回
* 没错这个可能就是关键

2. 所以， 既然一个管道stdin在没有数据时， read会被阻塞， 那么一个文件如果让它的结尾不是EOF， 是不是read的时候也会被阻塞？