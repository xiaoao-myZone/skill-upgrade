## shell 
### cp
1. `cp -r dir_a/* test/dir_b`
>> 会先将dir_b拷贝一份放入test/dir_b然后讲dir_a下面的所有文件放入test/dir_b 
2. cp理论上只能拷贝file,操作多个目录需要-r
3. 貌似cp默认情况下就会强制覆盖已存在的文件,不用加-f
