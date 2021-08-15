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

## create a table
1. CREATE TABLE test (
    colName int(11) NOT NULL,
    ...
) ENGINE=InnoDB DEFAULT CHARSET=utf-8;

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
## limit
limit `limit 1, 2` #从第二行开始取两行, `limit 3`是`limit 0, 3`的简略用法

## group by
1. select distinct 是它的特例
2. 在查询语句中处于from, where后面, 并且处于having,order by, limit前面 
3. group by value DESC # tips: 但是在标准sql中不允许加DESC到group by
4. 受count作用的启发, group by实际上是将table分成很多小table
5. 我猜想， group by后接的每一个字段， 抽出来去重做成了一个表， 并且有还有一个行号, 这样以来， group by存在两个值的时候，就像join一样， on的条件是就是行号

## join
### inner join
1. 只有当分别来自两个表的两行中指定的的字段"匹配", 才会将这两行合并为一行
2. 当两个表中被期望匹配的两个字段的匹配形式是`=`,并且他们的字段名也是一样的时候, 可以用using
3. 否则用更一般的匹配形式 `inner join on join_condition_expression`

### left join
1. 无论如何左边的表的内容都会选中,但是如果没有在右表中找到匹配项,就会用NULL代替右表中的值
### right join
1. 应该和左联接差不多, 但是如果一样,就没必要专门做一个右连接了(有时候为了格式方便)
### cross join
1. 完全地排列组合

### self join
1. 在一个表中自联, 必须将where中的表名与JOIN中的同一表名用别名(alias)区分开

## union
## functions
### aggregate function
1. sum
2. min/max
3. avg
4. count #数行数
5. concat
`select count(distinct state) from customers where country='USA'`
### others
1. field #如何将输出的结果按照某一个col的值的某种出现顺序排列
`select status from batch order by field(status, 'init', 'doing', 'done')`
接受一个变量,与其可能出现的枚举值,用来返回对应值的索引?
2. database #返回当前选中的数据库名
`select database()`
3. year 后面接一个date对象 #照理说也有month和day
4. concat_ws # 以第一个字符参数为间隙,连接后面的各个col的值
5. concat #拼接所有字段参数的值
6. group_concat 将group by得到的col进行组合

### 自定义函数
[参考](https://blog.csdn.net/helloxiaozhe/article/details/78124138)
CASE input_expression
WHEN when_expression THEN
    result_expression [...n ] [
ELSE
    else_result_expression
END

若没有指定 ELSE 子句，则返回 NULL 值

## having

1. 一般与group by 联用, 当没有group by 的时候相当于where
2. TODO 为什么having中的condition不能放在where中呢,我猜是为了提升查找速度
3. having与where的不同, having使用的变量是select中存在的,而不是表中存在的

## alias
1. funcion(col) as nickname
2. mysql支持group by 使用alias, 但是标准的sql语句不允许
3. 如果nickname中有空格,需要在两边用单引号括起来
4. ```select concat_ws(',', firstName,lastName) as `Full Name` from employees order by `Full Name`;``` #使用``时可以不用 as
5. <font color=#A52A2A>不可在where中引用alias, 因为mysql执行where的时候select还没有执行(信息量甚多)</font>
6. 给表创建别名 `select e.firstName, e.lastName from employees e order by e.firstName;`

### 书写顺序
1：select
2：from
3：left … join
4：on
5：where
6：group by
7：having
8：order by
9：limit

### 执行顺序
[参考](https://pig66.blog.csdn.net/article/details/51004754?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control)

1. from 
2. join 
3. on 
4. where 
5. group by(开始使用select中的别名，后面的语句中都可以使用)
6. avg,sum.... 
7. having 
8. select 
9. distinct 
10. order by
11. limit 


* group by 和 where的谁先执行?我猜是where



## some trick
1. 一登录就切换数据库
`mysql -u root -D dbname -p` #貌似不好使
2. 载入sql
`source /home/xiaoming/test.sql`
3. 不进入mysql客户端就输入指令
`mysql -u root -p -e "select 'hello'"`


## json




## 子查询(subquery)
1. 外部查询可以是SELECT INSERT, UPDATE, DELETE, DO和SET
2. FROM 也可以
3. 外部查询不能查询或修改内部查询所查的表, 不过FROM可以
4. 更细一点,子查询可以在这些语句的表达式中
5. 但是在select中， 貌似只能有一条单记录或者没有记录, 这且条记录中只能有一个字段

## 自定义函数
1. 函数貌似既不能输入也不能输出多条结果
DELIMITER $$
Create Function test(name varchar(20)) Returns varchar(50)
BEGIN
  DECLARE str VARCHAR(50) DEFAULT '';
  SET @tableName=name;
  SET str=CONCAT('create table ', @tableName,'(id int, name varchar(20));');
  return str;
END $$
DELIMITER ;

DELIMITER： 重定义结束符
变量需要申明: DECLARE
赋值需要用 SET

[MySQL之自定义函数](https://www.cnblogs.com/zhangminghui/p/4113160.html)

    


## 将行中的内容作为列
比如将某一课程的成绩作为作为放到新的字段中显示
1. group by && max(CASE WHEN cid='01' THEN score END)


## 事务
### 事务的概念
* 对数据库的优先操作序列构成，要么全部执行，要么全部不执行，是一个不可分割的工作单位
* mysql中只有innodb数据库引擎才支持事务
* 保证数据库的完整性
* insert update delete
* 开启事务： begin;/start transaction;
* 最后要么提交要么回滚
### 事务的特点
* 原子性: 要么完成要么不完成，没有中间态
* 一致性: 与完成前比较， 改动符合预期，包括精度
* 隔离性: 某一时刻只能处理一个事务
* 持久性: 一旦提交后， 不会被改动， 比如断电后重启

### 事务遇到的问题
* 脏读
* 不可重复读
* 幻读 (专指新插入的行)

[什么是幻读？以及如何解决幻读问题？](https://blog.csdn.net/new_buff_007/article/details/104249866?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control)
### 隔离级别
[面试问烂的 MySQL 四种隔离级别，看完吊打面试官！ - 良月柒的文章 - 知乎](https://zhuanlan.zhihu.com/p/76743929)
* 读未提交(read uncommitted)： 在一个事务中， 别的事务的未提交修改会影响到它的查询结果
* 读已提交(read committed): 别的事务的提交会影响它的查询
* 可重复读(repeatable read): 只有自己事务中的提交会影响到自己, 但同时也意味着， 别的事务插入的新行也不会被查询到
* 串行化(serializable): 若一个事务来查询同一份数据就必须等待，直到前一个事务完成并解除锁定为止。是完整的隔离级别，会锁定对应的数据表格，因而会有效率的问题（表锁）

## 索引
(MySQL索引是个什么东西)[https://zhuanlan.zhihu.com/p/101281323]
* 索引由一列或多列组合而成 ?
1. 逻辑上分： 唯一索引， 主键索引， 普通索引


## 乐观锁与悲观锁
1. 悲观锁应用到了真实的锁
2. 如果用CAS实现乐观锁， 那么乐观锁本质上不是锁， 是一种尝试， 往往会竞争失败

[什么是乐观锁，什么是悲观锁](https://www.jianshu.com/p/d2ac26ca6525)

## run sql script
1. 进入mysql交互界面, `source /home/userName/test.sql`
2. `$ mysql -u root -p -e "source /home/userName/test.sql"`



## 配置（无密码登录）
mysql_config_editor set --login-path=xiaoao --host=localhost --user=root --password --port=3306
mysql --login-path=xiaoao