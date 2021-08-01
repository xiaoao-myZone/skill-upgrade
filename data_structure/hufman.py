# -*- coding: utf-8 -*-
"""
1. 霍夫曼树最大的一个应用价值是可将字符进行不定长的编码/解码
2. 还可以根据字符的出现频率, 为每个字符设定不同长度的的编码, 这样可以在最小的带宽下实现最大的传输速率
3. 一言以蔽之, 霍夫曼编码可以实现, 任何一个字符的编码都不会是另一个字符的前缀
4. 它的二叉树结构有点像千足虫或者蜈蚣
"""

from pprint import pprint

def select(nums):
    """Select two list object which have the smallest weight."""
    index_map = [(i, val) for i, val in enumerate(nums)]
    index_map.sort(key=lambda x: x[-1][0])
    ret = []
    count = 0
    for i in index_map:
        if count == 2:
            break
        if i[1][1] == -1:
            ret.append(i[0])
            count+=1
    return ret

def build_tree(weight):
    n = len(weight)
    HT = [] #huffman tree
    # init
    for i in weight:
        HT.append([i, -1, -1, -1]) # weight, parent, lchild, rchild
    
    m = 2*n-1
    print(m)
    # the total length is m
    for i in range(n, m):
        HT.append([0 ,-1, -1, -1])

    # build
    for i in range(n, m):
        s1, s2 = select(HT[:i]) # s1<=s2, the sequenece of s1, s2 matter?
        HT[i][0] = HT[s1][0] + HT[s2][0]
        HT[s1][1] = i; HT[s2][1] = i
        HT[i][2] = s1; HT[i][3] = s2

    return HT 

def HuffmanCoding(HT):
    m = len(HT)
    n = (m+1)//2
    HC = [] #huffman code
    for i in range(m-1, -1, -1):
        HT[i][0] = 0

    count = 0
    
    code = []
    for i in range(n):
        HC.append('')
    i = m-1
    # 根据二叉树遍历的特点, 一个非子叶节点最多会被访问3次
    # from ipdb import set_trace; set_trace()
    while count<n:
            if HT[i][0] == 0: #第一次遍历
                HT[i][0] = 1 # 标记为访问过一次
                    
                if HT[i][2] != -1: # 有左孩
                    code.append(0)
                    #print("%d --> %d" % (i, HT[i][2]))
                    i = HT[i][2] # 第一次遍历, 找左孩
                    
                    
                else:# 找到一个编码
                    HC[i]= "".join(map(str, code))#应该是按顺序添加的
                    count+=1
                    #print("%d ends" % i)
                    #code = ''
            
            elif HT[i][0] == 1: #第二次遍历
                HT[i][0] = 2 #标记已第二次访问

                if HT[i][2] == -1: #没有左孩
                    pass #没有左孩一定没右孩
                else: 
                    code.append(1) #有右孩一定有左孩
                    #print("%d --> %d" % (i, HT[i][3]))
                    i = HT[i][3]
            else: # 第三次遍历
                HT[i][0] = 0 # 是否有必要? 没有必要
                #print("%d --> %d" % (i, HT[i][1]))
                i = HT[i][1]
                code.pop()

        
    return HC

def HuffmanDecoding(string, HT):
    ret = ''
    length = len(HT)
    p = length- 1
    for i in string:
        if i == '0': #0是取左还是右取决于编码的时候的选择
            p = HT[p][2]
        else:
            p = HT[p][3]
        
        if HT[p][2]==-1:  
            ret += HT[p][0]
            p = length- 1
            
    return ret


"""
Conclusion:
1. 只要是构建了二叉树, 就不会出现一个字符的编码是另一个字符的前缀的情况
2. 构建二叉树的时候有意将权重大的放到上层, 所以编码的时候权重越大, 位数越小
3. 这个构建二叉树的方式决定了它的不存度为1的节点, 即只有子叶节点和度为二的父节点
"""

            
    
if __name__ == "__main__":
    from pprint import pprint
    from collections import OrderedDict
    words_dict = {'a':5, 'b': 29, 'c': 7, 'd': 8, 'e': 14, 'f': 23, 'g': 3, 'h': 11}
    # keys与values的输出值是一一对应的
    words = list(words_dict.keys())
    weights = words_dict.values()
    print(words)
    print(weights)
    HT = build_tree(weights)
    pprint(HT)
    code_list = HuffmanCoding(HT)
    pprint(code_list) 
    # a:0001   b:10   c:1110   d:1111    e:110    f:01    g:0000    h:001 
    encode_word = '011101101111' # 'feed'

    for i in range(len(words)):
        HT[i][0] = words[i]

    ret = HuffmanDecoding(encode_word, HT)
    print(ret)

    