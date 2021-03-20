1. setsockopt
[setsockopt](https://blog.csdn.net/A493203176/article/details/70053137?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161529617416780266267434%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161529617416780266267434&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-70053137.first_rank_v2_pc_rank_v29&utm_term=setsockopt)

2. setblocking
    * 输入一个bool类型的参数
    * 默认是True
    * 当设置为False后,调用recv时,如果没有缓存区没有数据,那么抛出一个错误`socket.error: [Errno 11] Resource temporarily unavailable`

3. settimeout
    * 输入值是None或者int
    * None代表无限等待
    * int代表等待的秒数
    * TODO作用在哪个方法上?只有connect?