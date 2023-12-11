import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

def bfs(start, target):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if (x, y) == target:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len or ny < 0 or ny >= len:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[x][y]

t = int(input())

for _ in range(t):
    len = int(input())
    graph = [[0] * len for _ in range(len)]
    start = tuple(map(int, input().split()))
    target= tuple(map(int, input().split()))
    print(bfs(start, target))