## authority management
1. 查看所有用户
`select User, Host from mysql.user`
&#160;
2. 修改root用户密码(存疑)
`set password for 'dog'@'localhost' password("new_pw")`
&#160;
3. 创建用户并开放所有数据（还没有权限操作）
`grant usage on *.* to 'cat'@'localhost' identified by 'zxcasd';`
`show grants for "dog"@"localhost";`
`grant all on *.* to "dog"@"localhost";`
&#160;

## handle table
1. select
`select * from table_name where id<1000 order by id desc limit 4;`
&#160;
2. insert
`insert into table_name (col_1, col_2, ..) values(var_1, var_2, var_3...);`
&#160;


## know a table
1. 查看表的格式，注意describe的拼写
`describe tablename;` 