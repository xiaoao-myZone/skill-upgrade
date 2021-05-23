

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



#### 聚类
`SELECT Id from TabA group by Id;`
1. 可以查到Id这个col下有多少种值
2. SELECT后面如何加入非用来分类的col会报错, 直观上说原因很简单, 其值不唯一
3. 但是假设有两条Id = 2的记录, 那么使用group by后这两条记录是以何种形式存在的呢?或者如何继续对其进行操作?


