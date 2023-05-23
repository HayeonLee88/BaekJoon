# 1260 DFS와 BFS
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n + 1):
    graph[i].sort()

def DFS(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            DFS(i)

def BFS(start):
    visited[start] = True
    q = deque([start])
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

DFS(v)
print()
visited = [False] * (n + 1)
BFS(v)