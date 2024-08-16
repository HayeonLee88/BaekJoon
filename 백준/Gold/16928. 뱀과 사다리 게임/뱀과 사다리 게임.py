import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split()) # N개의 사다리, M개의 뱀

ladders = dict()
snakes = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snakes[x] = y

q = deque()
q.append((1, 0))

pos_l = ladders.keys()
pos_s = snakes.keys()
visited = [False] * (101)

while True:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        break
    for i in range(1, 7):
        nxt = now + i
        if nxt <= 100 and not visited[nxt]:
            if nxt in pos_l:
                nxt = ladders[nxt]
            elif nxt in pos_s:
                nxt = snakes[nxt]
            visited[nxt] = True
            q.append((nxt, cnt + 1))