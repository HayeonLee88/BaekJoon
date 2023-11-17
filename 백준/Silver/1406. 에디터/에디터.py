import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

q_left = deque(input())
q_right = deque()
n = int(input())

for _ in range(n):
    cmd = input()
    if cmd[0] == 'L':
        if q_left:
            q_right.appendleft(q_left.pop())
    elif cmd[0] == 'D':
        if q_right:
            q_left.append(q_right.popleft())
    elif cmd[0] == 'B': 
        if q_left:
            q_left.pop()
    else:
        q_left.append(cmd[-1])

print(''.join(c for c in q_left), end='')
print(''.join(c for c in q_right), end='')
