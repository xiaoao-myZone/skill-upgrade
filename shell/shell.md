## shell 
### cp
>> `cp  dir_a/* test/dir_b` 会先将dir_a拷贝一份放入test/dir_b然后讲dir_a下面的所有文件放入test/dir_b 
>> `cp -r dir_a test/dir_b` 
>> 
1. `cp  dir_a/* test/dir_b` 的前提是dir_a中没有目录只有文件
2. `cp -r dir_a test/dir_b` dir_b是否存在影响cp的行为,当dir_b存在时,dir_a会被拷贝后挪到dir_b下,当其不存在时,dir_a中的所有文件和目录都会挪到dir_b,而dir_a不在dir_b中
3. cp默认的被拷贝对象是文件,它所接受的非option参数只有被拷贝对象与目录,被拷贝对象可以有多个,用空格隔开
4. 貌似cp默认情况下就会强制覆盖已存在的文件,不用加-f

### mv
1. ''

### rm
1. 


### ps
[很详细](https://juejin.cn/post/6844903938144075783#heading-25)

### ls -l
[输出说明](https://blog.csdn.net/weixin_44903147/article/details/102480711)

### cat grep tr sort wc sed awk echo?
这个集合里的命令均将输入(stdin)的字符以一定方式转换再输出(stdout)出来

1. `cat` 输入文件路径 输出文件内容
2. `echo` 出入字符串, 原封不动输出字符串
3. `tr`  配置后, 输入字符串, 对字符串进行"增删改"后输出
4. `sort`
5. `wc` 对输入的字符数进行统计某种规则的字符统计, 输出结果
6. `sed`
7. `awk`


### script