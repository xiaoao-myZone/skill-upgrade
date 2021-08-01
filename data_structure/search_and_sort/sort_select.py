"""
Thinking:
1. 与冒泡排序基本一样， 不过是一次到位， 不再通过交换来一步步让最大值与最小值到达边缘
2. 如果在原数组的基础上一次遍历产出最大值与最小值， 在交换的时候涉及到4个数的交换， 
   这4个数中可能存在一对或者两对数相同， 操作不慎， 结果会出错
"""
def select_sort(nums):
    left, right, mini, maxim = 0, len(nums)-1, 0, 0
    while left<right:
        mini, maxim = left, right
        if nums[maxim]<nums[mini]:
            mini, maxim = maxim, mini

        for i in range(left+1, right):
            if nums[i]>nums[maxim]:
                maxim = i
            elif nums[i]<nums[mini]:
                mini = i
        nums[left], nums[mini] = nums[mini], nums[left]
        if maxim==left:
            maxim = mini # 此时最大值跑到了mini所在的位置
        # if mini==right: # 如果是先交换最右边与最大值， 则需要考虑这个
        #     pass
        nums[right], nums[maxim] = nums[maxim], nums[right]
        
        left+=1
        right-=1


if __name__ == "__main__":
    from random import shuffle
    nums = list(range(20))
    for i in range(10):
        shuffle(nums)
        res = sorted(nums)
        print("***第%d轮测试***" % i)
        print("\t输入: %s" % nums)
        select_sort(nums)
        print("\t输出: %s" % nums)
        if nums==res:
            print('\033[92m' + "### 通过 ###" + '\033[0m')
        else:
            print('\033[91m' + "### 失败 ###" + '\033[0m')
    
    ## left=0, right=4, mini=2, maxim=0
    ## [1, 2, 5, 4, 3] 
    ## [3, 2, 5, 4, 1]
    ## from ipdb import set_trace; set_trace()
    select_sort(nums)
    print(nums)
