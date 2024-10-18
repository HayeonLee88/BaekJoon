import sys
import heapq
from collections import defaultdict


input = lambda:sys.stdin.readline().rstrip()

T = int(input())
q_max = []
q_min = []

def check(dic, array, b):
    while True:
        num = heapq.heappop(array)
        if dic[b * num] != 0:
            break
    
    return b * num

for test_case in range(T):
    dict_ = defaultdict(int)
    q_max = []
    q_min = []
    cnt = 0
    k = int(input())
    for i in range(k):
        opt, n = input().split()
        n = int(n)
        if opt == 'I':
            cnt += 1
            dict_[n] += 1
            heapq.heappush(q_max, -n)
            heapq.heappush(q_min, n)
        else:
            if cnt == 0 :
                continue
            if n == 1:
                max_ = check(dict_, q_max, -1)
                dict_[max_] -= 1
            else:
                min_ = check(dict_, q_min, 1)
                dict_[min_] -= 1
            cnt -= 1
    if cnt:
        max_ = check(dict_, q_max, -1)
        min_ = check(dict_, q_min, 1)
        print(max_, min_)
    else:
        print('EMPTY')