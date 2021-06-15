"""
二分法查找有一个前提很容易被忽略, 那就是如何选择第一个查找的位置
这其实就是构建最优查找树的问题
本质上来说, 就是把最容易被查到的值放到最接近根节点的位置, 使得整体的查询次数期望最低 
"""

from binarytree import Node

def SecondOptinal():
    """次优查找树忽略了路径长度, 或者说假定路径长度一样
    """
    pass

def buildSearchTree(nums, ret, node=None):
    """迭代需要搞清楚每一次计算得到了什么, 在这个函数里就是给当前节点添加两个子叶
    Args:
        nums: a list or tuple, which need sorted.
        node: instance of `binarytree.Node`, or None
    """
    # (1,2,3,4,5,7,8)
    # 一个非子叶节点的左孩比它小, 右孩比它大
    # nums.sort()
    length = len(nums)
    if length == 0:
        return
    else:
        mid = length//2 # 偏右
        if node is None:
            node = Node(nums[mid])
            ret.append(node)
            if mid>0: # length is 1
                buildSearchTree(nums[:mid], ret, node)
                buildSearchTree(nums[mid+1:], ret, node)
            
        else:
            if node.left is None: # 先序构建
                node.left = Node(nums[mid])
                buildSearchTree(nums[:mid], ret, node.left)
                buildSearchTree(nums[mid+1:], ret, node.left)
            else:
                node.right = Node(nums[mid])
                buildSearchTree(nums[mid+1:], ret, node.right)
                buildSearchTree(nums[:mid], ret, node.right)

nums = [1,2,3,4,5,6,7,18]
ret = []
root = Node(0)
buildSearchTree(nums, ret)
print(ret)
print(ret[0])
print(root)