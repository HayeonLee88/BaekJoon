'''
8:58~
'''
from math import gcd
def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        gcd_ = gcd(answer, num)
        answer = (answer * num) // gcd_
    return answer