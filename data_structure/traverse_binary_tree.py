# -*- coding: utf-8 -*-

class BinNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.lChild = left_child
        self.rChild = right_child
        self.value = value
    
    def addLeft(self, lChild):
        self.lChild = lChild
    
    def addRight(self, rChild):
        self.rChild = rChild
    
    def add(self, child):
        if self.lChild is None:
            self.lChild = child
        elif self.rChild is None:
            self.rChild = child
        else:
            raise Exception("Couldn't add the third child")
    
    def headTraverse(self, ret):
        ret.append(self.value)
        if self.lChild:
            self.lChild.headTraverse(ret)
            if self.rChild:
                self.rChild.headTraverse(ret)
    
    def midTraverse(self, ret):
        if self.lChild:
            self.lChild.midTraverse(ret)
        ret.append(self.value)
        if self.rChild:
            self.rChild.midTraverse(ret)

    def rearTraverse(self, ret):
        if self.lChild:
            self.lChild.rearTraverse(ret)
            if self.rChild:
                self.rChild.rearTraverse(ret)
        ret.append(self.value)



class TriNode(BinNode):
    def __init__(self, value, root, left_child=None, right_child=None, ):
        super(TriNode, self).__init__(value, left_child, right_child)
        self.root = root


def buildTree(nums):
    if nums is 0:
        return None
    tmp = nums
    root = BinNode(0)
    nums -= 1
    layer = [root] * 2
    while nums:
        new = BinNode(tmp-nums)
        layer.pop(0).add(new)
        layer.append(new)
        layer.append(new)
        nums-=1
    return root

nums = 10
root = buildTree(nums)
ret = []
root.headTraverse(ret)
print(ret)
ret = []
root.midTraverse(ret)
print(ret)
ret = []
root.rearTraverse(ret)
print(ret)

"""
                    0

             /             \
            1               2
         /      \        /      \
        3        4      5        6   
       / \      / \    / \      / \
      7   8    9   10
"""

