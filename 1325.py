# 1325번: 효율적인 해킹
from collections import deque
import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)

count = 1


def BFS(start):
    cnt = 0
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        cnt += 1
        now = q.popleft()
        for trustedBy in graph[now]:
            if visited[trustedBy]:
                continue
            visited[trustedBy] = True
            q.append(trustedBy)
    return cnt


answer = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    tmp = BFS(i)
    if tmp > count:
        count = tmp
        answer = [i]
    elif tmp == count:
        answer.append(i)

print(*answer)
