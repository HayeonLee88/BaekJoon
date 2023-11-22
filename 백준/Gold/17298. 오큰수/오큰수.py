import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
seq = list(map(int, input().split()))

stack = []
answer = deque()
for i in range(n - 1, -1, -1):
    now = seq[i]
    while stack and now >= stack[-1]:
        stack.pop()
    if stack:
        answer.appendleft(stack[-1])
    else:
        answer.appendleft(-1)
    stack.append(now)

print(*answer)
