import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = deque()

for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'size': # q에 정수가 있든 없든 상관없이 똑같이 실행되는 명령
        print(len(q))
    elif cmd[0] == 'push': 
        q.append(cmd[-1])
    else:
        if q:
            if cmd[0] == 'pop':
                print(q.popleft())
            elif cmd[0] == 'front':
                print(q[0])
            elif cmd[0] == 'back':
                print(q[-1])
            else: # empty
                print(0)
        else:
            if cmd[0] in ['pop', 'front', 'back']:
                print(-1)
            else : # empty
                print(1)
                