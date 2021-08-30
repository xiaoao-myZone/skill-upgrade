## 安装

sudo apt-get install redis-server
(会自动安装redis-cli)
## redis技巧与注意事项

1. 避免所有时间复杂度超过O(1)的操作, 比如del, lrange, linsert

## 应用案例
1. 游戏或者话题排名用有序集合
[Redis基础 常用类型 时间复杂度](https://blog.csdn.net/Andy86869/article/details/88366513)
[面试官：你遇到 Redis 线上连接超时一般如何处理？](https://zhuanlan.zhihu.com/p/143811218)
[redis数据类型 评论](https://www.runoob.com/redis/redis-data-types.html)