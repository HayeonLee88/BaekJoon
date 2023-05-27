# 2693번: N번째 큰 수
import sys
t = int(input())
for _ in range(t):
    array = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    print(array[-3])
