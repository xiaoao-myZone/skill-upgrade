

### 左连与右连

#### 样例
1. `SELECT * from TabA LEFT JOIN TabB on TabA.Id = TabB.Id;`
2. `SELECT * from TabA RIGHT JOIN TabB on TabA.Id = TabB.Id;`
3. `SELECT * from TabB RIGHT JOIN TabA on TabA.Id = TabB.Id;`
4. `SELECT * from TabB LEFT JOIN TabA on TabA.Id = TabB.Id;`

#### 总结
1. 左连与右连并不是表拼接的顺序, 对以上四个例子, 表的拼接顺序与其在sql语句出现的顺序一致(从左至右)
2. 左连与右连的意义在于选择哪个表作为驱动, 或者说, 如果将这个搜索用python实现, 需要两个for循环, 哪个表作为外循环, 哪个作为内循环
3. 显然哪个作为外循环(选择哪个表作为驱动), 查询次数和结果是不一样的
4. 某个字段在两个表中分别存在一个集合, 选择子集作为驱动, 可以减少查询次数, 并且输出不会有多余的NULL存在
5. 问题在于在python中， 内外两个循环，无论谁在内谁在外， 搜索的数量都是一样的， n*m，唯一的可能是， 对外循环是遍历， 对内循环是哈希索引？ 猜想正确， 同时要补充， 如果一个外查询有过滤则会每次循环都过滤一遍
[写出好的Join语句，前提你得懂这些 - 月伴飞鱼的文章 - 知乎](https://zhuanlan.zhihu.com/p/336637328)



### 聚类
`SELECT Id from TabA group by Id;`
1. 可以查到Id这个col下有多少种值
2. SELECT后面如何加入非用来分类的col会报错, 直观上说原因很简单, 其值不唯一
3. 但是假设有两条Id = 2的记录, 那么使用group by后这两条记录是以何种形式存在的呢?或者如何继续对其进行操作?

[MySql中取出每个分组中的前N条记录](https://blog.csdn.net/hudie1234567/article/details/6258420?utm_source=blogxgwz21&utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.control&spm=1001.2101.3001.4242)




### SUM
1. 与NULL比较大小, 返回值是NULL
2. MAX中NULL比正数小, 与0相比呢? TODO

### on 与 where
从原理上来看： on在where之前执行， on与join联用作用于表的生成， 而where只会在表生成后起作用
从结果上来看： on的结果可能会有null（当驱动表中的值在被驱动表中不存在时），但是where不会

### in 与 exist


### 可用子查询取代的地方
1. select
2. from
3. where
4. group by
5. having

当子查询只返回一行一列时，可以当做一个变量来处理， 可以代替select， on, where等中的col_name


### group by
1. 最大的好处是去重
2. 对某一字段的所有结果进行统计分析
3. 

### 与NULL较真
1. 当结果是empty的时候，可以用`select (...) as result;`来获得NULL
2. inner join可以避免出现两表出现没有匹配而产生的NULL
3. IFNULL, 当返回值是null或者emtpy的时候返回后者
4. 当函数返回结果是int时， empty和NULL都能正常接收



