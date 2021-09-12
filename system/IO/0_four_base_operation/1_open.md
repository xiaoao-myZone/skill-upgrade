# Open


`fd = open(filepath, flag, mode)`
1. filepath可以是符号链接， open会对其进行解引用
2. flag由O_READONLY O_WRONLY O_RDWR O_CREAT O_TRUNC O_APPEND
3. S_IRUSR  S_IWGRP  S_IXOTH
4. fd始终按最小未使用的取值
* fd一定是某个数组的索引， 那么它的长度有多大呢？这个可以通过ulimit或者setrlimit来修改