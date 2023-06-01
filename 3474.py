# 3474 교수가 된 현우

import sys
input = lambda: sys.stdin.readline().rstrip() # 시간초과 날 때 빠르게 읽기
n = int(input())

for i in range(n):
    num = int(input())
    cnt = num//5
    tmp = cnt
    while tmp > 1:
        tmp //= 5
        cnt += tmp
    print(cnt)