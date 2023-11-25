import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = deque()

for i in range(n):
    cmd_list = list(input().split())
    cmd = cmd_list[0]
    if cmd == "pop_front":
        print(q.popleft() if q else -1)
    elif cmd == "pop_back":
        print(q.pop() if q else -1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(0 if q else 1)
    elif cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "back":
        print(q[-1] if q else -1)
    elif cmd == "push_front":
        q.appendleft(cmd_list[-1])
    else:
        q.append(cmd_list[-1])
