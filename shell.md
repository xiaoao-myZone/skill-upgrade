## shell 
### cp
>> `cp  dir_a/* test/dir_b` 会先将dir_a拷贝一份放入test/dir_b然后讲dir_a下面的所有文件放入test/dir_b 
>> `cp -r dir_a test/dir_b` dir_a将会出现在dir_b目录下,并且dir_b/dir_a中的内容与原来的dir_a完全相同
>> 
1. `cp  dir_a/* test/dir_b` 的前提是dir_a中没有目录只有文件
2. cp默认的被拷贝对象是文件,它所接受的非option参数只有被拷贝对象与目录,被拷贝对象可以有多个,用空格隔开
3. 貌似cp默认情况下就会强制覆盖已存在的文件,不用加-f

### mv
1. ''

### rm
1. 
