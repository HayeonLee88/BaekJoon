from math import sqrt

def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        now = int(sqrt(num))
        if now * now == num:
            answer -= num
        else:
            answer += num
    return answer