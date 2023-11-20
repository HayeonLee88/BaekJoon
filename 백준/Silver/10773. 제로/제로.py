from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

stack = deque()
for i in range(int(input())):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))