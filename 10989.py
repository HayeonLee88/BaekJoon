# 10989번: 수 정렬하기 3
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
cnt = [0] * 10001
for _ in range(n):
    cnt[int(input())] += 1
for index, num in enumerate(cnt):
    if num == 0:
        continue
    for i in range(num):
        print(index)