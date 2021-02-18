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
`select * from table_name where id<1000 order by id desc/asc, name desc/asc limit 4;`
执行顺序: from -> where -> select -> order by
&#160;
2. insert
`insert into table_name (col_1, col_2, ..) values(var_1, var_2, var_3...);`
&#160;


## know a table
1. 查看表的格式，注意describe的拼写
`describe tablename;`
describe 可以简写为 desc
2. 与1相同
`show columns from tablename;`
3. 查看各列更详细的信息
`show full columns from tablename;`


## select
1. columns可以通过表达式运算后显示出来
`select price * saleNum from sale;`
2. 如果嫌表达式太长,可以起一个别名
`select price * saleNum as sum from sale;`

## where
1. = > <
2. AND OR
3. varname between a and b
4. like `col like %son` result is Json, handson
5. in `col in (1,2,3)`
6. is `col is NULL` 不能用=NULL
## function
1. field
`select status from batch order by field(status, 'init', 'doing', 'done')`
接受一个变量,与其可能出现的枚举值,用来返回对应值的索引?
2. 