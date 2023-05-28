# 11650번: 좌표 정렬하기
import sys

n = int(input())
dots = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dots.sort(key=lambda x: x[1])
dots.sort(key=lambda x: x[0])
for dot in dots:
    print(dot[0], dot[1])
