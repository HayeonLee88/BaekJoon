# 2636번: 치즈 (BFS, 그래프)

import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    num = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
            elif graph[nx][ny] == 1: # 치즈는 append를 하지 않고 가장자리만 0으로 녹게 한다.
                num += 1
                visited[nx][ny] = True
                graph[nx][ny] = 0
    return num

time = 0
melted_cheese = []
while True:
    visited = [[False]*m for _ in range(n)]
    melted_cheese.append(BFS(0, 0))
    if not melted_cheese[-1]:
        print(time)
        print(melted_cheese[-2])
        break
    time += 1


'''
방법2
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 1 or visited[nx][ny]:
                continue
            graph[nx][ny] = 2
            q.append((nx, ny))
            visited[nx][ny] = True
cnt = 0
w = []
while True:
    visited = [[False] * m for _ in range(n)]
    bfs(0, 0)

    melted_list = [] 
    tmp = 0 
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == 1: 
                tmp += 1
                if graph[i + 1][j] == 2 or graph[i - 1][j] == 2 or graph[i][j + 1] == 2 or graph[i][j - 1] == 2:
                    melted_list.append([i, j])
    cnt += 1
    if len(melted_list) == tmp:
        print(cnt)
        print(tmp)
        break
    for x, y in melted_list:
        graph[x][y] = 2
'''