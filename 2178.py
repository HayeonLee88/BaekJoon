# 2178번: 미로 탐색 BFS 넓이 우선 탐색

import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
move_x = [-1, 1, 0, 0] # 상 하 좌 우
move_y = [0, 0, -1, 1]
graph = []

for i in range(n):
    graph.append(list(map(int, input()))) # 공백없는 문자열은 split()할 필요가 없다

def BFS(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[x][y]

print(BFS(0, 0))