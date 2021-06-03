## data structure note


### 二叉树
1. 二叉树与折半查找(二分法求值)
* 二叉树是折半查找的时间历程模型
* 折半(2的等比数列)查找还可以泛化为斐波拉契查找, 或者以其他的发散数列为基础的查找模型

2. 霍夫曼二叉树
* 在编码方面十分有用
* 特点是每一个子叶节点的路径都是不是另外节点的路径的前段
* 如果一个报文只有4中字母, 用两个比特确实可以解决问题, 但是用霍夫曼编码(0, 10, 110, 111)可以解决当这四个字母在报文中出现的频率不一样时, 可以使高频字母用最短的编码表示, 在各个字母中频率差距较大时, 使用霍夫曼编码可以减小所需带宽

3. 平衡二叉树
* 平衡因子: 一个节点的左子树深度与右子树的深度差
* 平衡二叉树的平衡因子绝对值不大于2
* 平衡二叉树的意义在哪