'''
3:58~
같은 종류 == 같은 번호
'''
from collections import defaultdict

def solution(nums):
    answer = 0
    dict_ = defaultdict(int)
    for num in nums:
        dict_[num] += 1
    
    types = len(dict_.keys())
    if len(nums) // 2 <= types:
        return len(nums) // 2
    return types