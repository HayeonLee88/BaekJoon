import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = deque()

for i in range(n):
    cmd = input()
    if cmd == "pop_front":
        print(q.popleft() if q else -1)
    if cmd == "pop_back":
        print(q.pop() if q else -1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(0 if q else 1)
    elif cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "back":
        print(q[-1] if q else -1)
    else: # append
        cmd = list(cmd.split())
        if cmd[0] == "push_front":
            q.appendleft(cmd[-1])
        elif cmd[0] == "push_back":
            q.append(cmd[-1])
