# 2606번: 바이러스
import sys
from collections import deque

n = int(input())
k = int(input())
network = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    network[a].append(b)
    network[b].append(a)

def BFS(start):
    count = 0
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for connect in network[now]:
            if visited[connect]:
                continue
            visited[connect] = True
            count += 1
            q.append(connect)
    return count

print(BFS(1))
