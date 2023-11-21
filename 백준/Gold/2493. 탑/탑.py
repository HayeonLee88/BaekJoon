import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
top_heights = list(map(int, input().split()))
stack = []

answer = []
for i, h in enumerate(top_heights):
    while stack:
        if stack[-1][1] >= h:
            answer.append(stack[-1][0] + 1)
            stack.append((i, h))
            break
        else:
            stack.pop()
    if not stack:
        stack.append((0, 0))
        answer.append(0)
        stack.append((i, h))

print(*answer)