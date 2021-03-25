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

Question: select到底如何理解?
&#160;



## know a table
1. 查看表的格式，注意describe的拼写
`describe tablename;`
describe 可以简写为 desc
2. 与1相同
`show columns from tablename;`
3. 查看各列更详细的信息
`show full columns from tablename;`
4. 查看某一字段的值的所有种类
`select distinct column_name from tablename;`
5. 查看表的记录条数
`select count(*) from tablename;`
6. 查看字段的组合种类
`select distinct column_name_1, column_name_2 from tablename;`
7. 查看字段出现的频次
`select col_name, count(*) from tablename group by col_name;`
8. 二次查询(比如找到一种字段组合出现过两次的所有记录) TODO
`select col_name_1, col_name_2, count(*) from tablename group by col_name_1, col_name_2;`

## select
1. columns可以通过表达式运算后显示出来
`select price * saleNum from sale;`
2. 如果嫌表达式太长,可以起一个别名
`select price * saleNum as sum from sale;`
3. distinct跟在select后面作为修饰,只在相同的值中获取一行
>> 这会有一个小问题,它到底会选哪一行? 
* 貌似选不了,指示做一个set的操作
>> 如果后面跟多个col会怎么样? 
* 会将多个col的组合起来作为原来的col

## where
1. = > <
2. AND `boolean_expression_1 AND boolean_expression_2` OR
3. varname between a and b
4. like `col like %son` result is Json, handson
5. in `col in (1,2,3)` #与python中的in相同
6. is `col is NULL` 不能用=NULL
7. limit `limit 1, 2` #从第二行开始取两行, `limit 3`是`limit 0, 3`的简略用法

## group by
1. select distinct 是它的特例
2. 在查询语句中处于from, where后面, 并且处于having,order by, limit前面 
3. group by value DESC # tips: 但是在标准sql中不允许加DESC到group by
## functions
1. field #如何将输出的结果按照某一个col的值的某种出现顺序排列
`select status from batch order by field(status, 'init', 'doing', 'done')`
接受一个变量,与其可能出现的枚举值,用来返回对应值的索引?
2. database #返回当前选中的数据库名
`select database()`
3. count #数行数
`select count(distinct state) from customers where country='USA'`
4. sum
5. min/max
6. avg
7. year 后面接一个date对象

## having

1. 一般与group by 联用, 当没有group by 的时候相当于where
2. TODO 为什么having中的condition不能放在where中呢,我猜是为了提升查找速度
3. having与where的不同, having使用的变量是select中存在的,而不是表中存在的

## alias
1. funcion(col) as nickname
2. mysql支持group by 使用alias, 但是标准的sql语句不允许




## some trick
1. 一登录就切换数据库
`mysql -u root -D dbname -p`
2. 载入sql
`source /home/xiaoming/test.sql`
3. 不进入mysql客户端就输入指令
`mysql -u root -p -e "select 'hello'"`