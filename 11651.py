# 11651번: 좌표 정렬하기 2
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]
dots.sort(key=lambda x: x[0])
dots.sort(key=lambda x: x[1])
for dot in dots:
    print(dot[0], dot[1])
