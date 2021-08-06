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

## 配置
### 获取配置
`redis-cli> CONFIG GET port`
### 配置
1. port
2. bind     可接入的ip 
3. backlog  最大连接数 
4. time     客户端最大不活跃时间
5. loglevel 日至等级
6. logfile  日志路径 (有最大size限制吗)
7. syslog-enable    是否记录到log文件

## 使用
### 通用
1. 操作成功返回0， 失败1
2. 在redis-cli中，给一个命令开头， 不断按tab, 会出现各种可能值

### shell命令行使用
>> 进入redis-cli
1. select 0 # 第一个逻辑数据库
2. set/get 
`set test hello` 
`get test` 
`del test`
3. HMSET/HGET/HDEL
`HMSET dict-like a "nice" b "not bad"`
`HGET dict-like a`
`HDEL dict-like`
>> HDEL的效果貌似与DEL相同
>> 如何添加？如何删除其中的k-v对
>> HMGET和HGET有何区别
4. lpush/lrange/lpop
`lpush list-like "python"`
`lpush list-like "golang"`
`lrange list-like 0 10` 闭区间， 不是左闭右开，可以超范围
`lpop list-like` 只会将队首的数值弹出， 是一个天然的队列，而不能做成栈
>> 可以加入不同类型的数据吗？比如string和int?
5. sadd/smembers 集合
>> 只能是string类型

6. zadd 有序集合
zadd set-like 4 miss
>> 只能是string类型
>> 分数可以重复， 并且是double类型


### 用python使用

### 用golang使用

### 图形客户端工具

## 各数据类用法总结
1. String(字符串) 	二进制安全 	    可以包含任何数据,比如jpg图片或者序列化的对象,一个键最大能存储512M 	---
2. Hash(字典) 	    键值对集合,即编程语言中的Map类型 	适合存储对象,并且可以像数据库中update一个属性一样只修改某一项属性值(Memcached中需要取出整个字符串反序列化成对象修改完再序列化存回去) 	存储、读取、修改用户属性
3. List(列表) 	        链表(双向链表) 	增删快,提供了操作某一段元素的API 	1,最新消息排行等功能(比如朋友圈的时间线) 2,消息队列
4. Set(集合) 	哈希表实现,元素不重复 	1、添加、删除,查找的复杂度都是O(1) 2、为集合提供了求交集、并集、差集等操作 	1、共同好友 2、利用唯一性,统计访问网站的所有独立ip 3、好友推荐时,根据tag求交集,大于某个阈值就可以推荐
5. Sorted Set(有序集合) 	将Set中的元素增加一个权重参数score,元素按score有序排列 	数据插入集合时,已经进行天然排序 	1、排行榜 2、带权重的消息队列

[redis教程](https://www.runoob.com/redis/redis-conf.html)