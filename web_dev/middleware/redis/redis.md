# Redis


## 准备知识
热数据: 使用率高的数据
随机读取： 读写时间与存取的地址无关， 比如hash？

从内存中顺序读取速度是从硬盘读取速度的6倍
从内存中随机读取速度是从硬盘读取速度的10w倍

>> 注意： 数据库中相关数据被修改， 需要同步到缓存中，同时缓存中的数据是从数据库中读出来的


## 案例分析

1. 淘宝双11策略： 下的单先写入高速缓存集群， 再延时写入数据集
2. 抢购时， 当商品没有了， 可以下单成功， 但是支付时失败，造成不好的用户体验

这是因为下单直接请求数据库， 并发时， 先向数据库中读， 这时是有的， 但是当超量的订单一个个改写数据库， 就会有的失败

可以用高速缓存来解决， 它是一个个去处理请求的（读与写），数据库不可以这样因为延迟会很高， 然后再把结果写入数据库

## 标签
1. Nosql  
2. C开发  
3. 10wQPS(来自官方)， 官方只支持linux
4. 随着连接redis的用户增加， QPS会变慢， 4w个连接数后， 性能变为原来一半， 6w可以达到4w+QPS
5. MYSQL一般支撑几千个连接

## 安装与启动
`sudo apt-get install redis-server` 一般安装后会自己启动
`sudo systemctl status redis` 查看状态

>> 修改配置后需要重启

## 配置
### 获取配置
`redis-cli> CONFIG GET port`
### 配置
#### 基础设置
1. port
2. bind     可接入的ip 
3. backlog  最大连接数 
4. time     客户端最大不活跃时间
5. loglevel 日至等级
6. logfile  日志路径 (有最大size限制吗)
7. syslog-enable    是否记录到log文件
#### 中级设置
1. databases
2. save  "900 1 300 10 60 10000"  # 第一个值是同步到rdb的频率
3. rdbcompression 
4. dbfilename
5. dir
6. requirepass
#### 高级
1. maxclient 最大客户连接数 (达到最大连接数会怎么样？)
2. maxmemory 最大内存占用
3. appendonly AOF 持久化方案 会取代rdb
4. appendfsync AOF同步频率 no|everysec|always  
## 使用
### 通用
1. 操作成功返回1， 失败0
2. 在redis-cli中，给一个命令开头， 不断按tab, 会出现各种可能值

### shell命令行使用
>> 进入redis-cli
1. select 0 # 第一个逻辑数据库
2. string set/get (其实它即可以代表string也可以代表int)
`set test hello` 
`get test` 
`del test`
`getrange test 0 1` # 截取, 两边都是闭区间
`strlen test`
`append test ",world"`
`setex foo 20 baga` # 设置同时设计过期时间(s)
`psetex foo ` # 过期时间为ms
>> 数字操作
`INCR/DECR` 操作的数据类型必须是整形数字, ++/--
`INCRBY/DESRBY` 加减一个具体的数值 +=/-=
3. hash表
`HMSET dict-like a "nice" b "not bad" c 10`
`HGET dict-like a`
`HDEL dict-like a`
`HGETALL dict-like` 返回所有键值
`HEXISTS dict-like a` 
`HVALS dict-like`
`HKEYS dict-like`
`HINCRBY dict-like c 2`  HINCRBYFLOAT
``
>> HDEL的效果貌似与DEL相同 (HDEL 除了变量名 还需要hash的键)
>> 如何添加？如何删除其中的k-v对
>> HMGET和HGET有何区别
4. 数列
`lpush list-like "python"` 从队首加入队列
`rpush` 从队尾加入
`lpop` 从队首弹出
`rpop` 从队尾弹出
`lrange list-like 0 10` 闭区间， 不是左闭右开，可以超范围
`lrange list-like 0 -1` -1表示遍历到底
`linsert list-like after l ll`  在队列中搜索出l，然后在它的后面加上ll
`rpoplpush` 将一个队列的队尾弹出并加到另一个队列的队首
`llen`
`lindex list-like index` 根据索引取值
`lrem`
`lset list-like index value` 根据索引赋值
`ltrim`
`lpushx`
`rpushx`

>> lrange貌似没办法逆序输出
>> 相同的前缀push与pop结合， 形成栈， 不相同的形成队列
>> 为什么没有通过索引插入的操作??
5. 集合
`sadd set-like a b c`
`spop set-like` 按具体的当前的顺序（这个顺序随机生成），随机弹出, 宏观来看就是随机
`smembers set-like` 查询所有元素
`sismember set-like a`
`scard set-like` 集合的长度
`srandomember set-like 3` 随机顺序， 如果超出长度，不会报错， 不会删掉, 没有数量默认为1
`sscan set-a 0 match * count 1`  key名后面是游标， match 匹配对象 count是搜索次数，而不是最后的结果数
`srem set-a a b c` 移除一个或多个元素

[scan中游标的意义](https://www.cnblogs.com/Mike_Chang/p/9499625.html)
集合间的运算
`sdiff set-a set-b` 前者对后者的差异
`sinter set-a set-b` 两个集合的交集
`sinterstore d set-a set-b` 交集存在d中
`smove set-a element set-b` 从a将element移动到b
`sunion set-a set-b` 求并集
`sunionstore d set-a set-b` 求并集并存储

>> 只能是string类型
>> redis不能区分空set与list
>> 蛮好奇， 既然smembers是按hash值的顺序输出的， 那么为什么pop与randomember还是乱序的呢？

6. zadd 有序集合
zadd set-like 4 miss
>> 只能是string类型
>> 分数可以重复， 并且是double类型


### 用python使用

### 用golang使用

### 图形客户端工具

## 各数据类用法总结
1. String(字符串) 	二进制安全 	    可以包含任何数据,比如jpg图片或者序列化的对象,一个键最大能存储512M 	---
2. Hash(字典) (h)	    键值对集合,即编程语言中的Map类型 	适合存储对象,并且可以像数据库中update一个属性一样只修改某一项属性值(Memcached中需要取出整个字符串反序列化成对象修改完再序列化存回去) 	存储、读取、修改用户属性
3. List(列表) (l) 	        链表(双向链表) 	增删快,提供了操作某一段元素的API 	1,最新消息排行等功能(比如朋友圈的时间线) 2,消息队列
4. Set(集合) (s)	哈希表实现,元素不重复 	1、添加、删除,查找的复杂度都是O(1) 2、为集合提供了求交集、并集、差集等操作 	1、共同好友 2、利用唯一性,统计访问网站的所有独立ip 3、好友推荐时,根据tag求交集,大于某个阈值就可以推荐
5. Sorted Set(有序集合) (z)	将Set中的元素增加一个权重参数score,元素按score有序排列 	数据插入集合时,已经进行天然排序 	1、排行榜 2、带权重的消息队列
6. stream（x）
7. (r)



### 参考：
1. redis既具有存储功能也具有一定的数据处理功能 [redis教程](https://www.runoob.com/redis/redis-conf.html)
2. [RDB和AOF的区别](https://www.cnblogs.com/zxs117/p/11242026.html)

### 阅读总结
[把Redis当作队列来用，真的合适吗？ ](https://mp.weixin.qq.com/s/-rHlfVsmrKrouvJh2YnxbA)
1. redis可以非常容易地实现生产者-消费者模型， LPUSH与RPOP就是入栈与出栈操作， 如果消费者需要阻塞， 使用BRPOP， 或者BLPOP， B就是Block的意思, 并且还可以带超时参数，与epoll.poll一样
>> 不过要注意， 太长时间不活跃的链接会被redis主动关闭，客户端需要有重连机制
2. 这种消息队列的缺点是不可以支持重复消费， 并且当客户端拉取消息后，如果宕机， 就永久地丢失这个数据了（讲道理这个问题真的有点强人所难）
3. Publish/Subscribe模型可以解决重复消费的问题, 同时可以明确的是， 这里的重复消费是指， 不同的客户端对同一个消息的消费， 但是我猜， 其本质是将收集订阅的客户端， 然后消息收到后主动推送一波（PUBLISH queue/SUBSCRIBE queue/PSUBSCRIBE queue.*）
4. 这种模式会存在因 redis宕机， 客户端下线， 消息堆积（客户端数据处理不足）造成的消息丢失问题
5. 数据持久化比如(RDB和AOF)
6. TODO redis的stream在收到XACK后， 是如何删除数据的？ 1. 如果为每个客户端创建一个队列内存会根据客户端连接数线性扩大，收到XACK后理论上可以立即删除 2.如果多个客户端共用一个队列， 那么需要这些客户端都发送了XACK才能删掉。
7. 网络异常（1. 无法连接  2. 已发送但是没有响应， 重发若干次然后记为异常）
8. 消息队列的几个问题（1. 生产者是否会消息丢失 2. 消费者是否会消息丢失 3. 中间件是否会消息丢失 4. 如果消息挤压要怎么办）