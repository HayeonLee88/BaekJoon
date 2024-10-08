import sys
from collections import deque

n = int(input())
data = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n + 1)
answer = [0] * (n + 1)

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for node in data[now]:
            if visited[node]:
                continue
            visited[node] = True
            answer[node] = now
            q.append(node)

BFS(1)
for i in range(2, n + 1):
    print(answer[i])