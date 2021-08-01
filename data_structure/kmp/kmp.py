"""
Thinking:
1. 待匹配的子字串需要有重复部分
2. 并且从头开始的一段存在于这写重复部分中
3. 需要一个辅助数组记录其匹配失败后， 可以从哪部分继续开始， 而不一定是从头开始
4. 如果不是从头开始， 一定是在匹配一段自身存在该处重复的部分
5. 如果能匹配到这里吗说明目标父串亦存在相同情况重复部分
"""


def kmp(pattern, target):
    """
    Args:
        pattern: str
        target: str

    Returns:
        int, means the start index of substring of target
        and -1 means the pattern is not the substring.
    """
    length = len(pattern)
    i, j = 0, 1
    nums = [0] * (length+1) #加一是为了应对nums[-1]的情况
    while j<length:
        if pattern[i] == pattern[j]:
            nums[j] = i+1 # 存放的是j处如果与目标匹配不上, 可以回跳的地方
            i+=1

        else:
            # i = nums[j-1] # TODO make sure 
            i = 0 # 直接回到原点
        j+=1
    print(nums)
    len(target)
    i, j = 0, 0
    target_len = len(target)
    # from ipdb import set_trace; set_trace()
    while j<target_len and i<length:
        if target[j] == pattern[i]:
            j+=1
            i+=1
        elif i==0:
            j+=1
        else:
            i = nums[i-1]
    
    if i ==length:
        return j-length
    else:
        return -1

if __name__ == "__main__":
    pattern = 'bcabcae'
    target = "aaaabcabcabcaeby"
    ret = kmp(pattern, target)
    print(ret)