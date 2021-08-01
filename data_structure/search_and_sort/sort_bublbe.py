"""
1. 从头开始循环， 相邻两两比较，将较大者往后移
2. 内部循环每次从队尾减少一， 因为上一步已经将正确的值放到了正确的位置
3. 时间复杂度是n^2， (n-1)(n-2)/2当数组正好逆序时
"""


def bubble(nums):
    lenght = len(nums)
    tmp = 0
    for i in range(lenght):
        for j in range(1, lenght-i):
            tmp = j-1
            if nums[tmp]>nums[j]:
                nums[tmp], nums[j] = nums[j], nums[tmp]

if __name__ == "__main__":
    nums = [5,2,1,4,3]
    bubble(nums)
    print(nums)
