# 1303번: 전쟁 - 전투
# DFS/BFS
import sys
from collections import deque

sys.setrecursionlimit(30001)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]


def DFS(x, y, color):
    global cnt
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[x][y] == color:
        cnt += 1
        graph[x][y] = 0
        DFS(x - 1, y, color)
        DFS(x + 1, y, color)
        DFS(x, y - 1, color)
        DFS(x, y + 1, color)
        return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    q = deque()
    q.append((x, y))
    color = graph[x][y]
    graph[x][y] = count = 0
    while q:
        count += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == color:
                q.append((nx, ny))
                graph[nx][ny] = 0

    return count*count

answer = [0, 0]
'''
for i in range(m):
    for j in range(n):
        cnt = 0
        if graph[i][j] == 'W':
            DFS(i, j, 'W')
            answer[0] += cnt * cnt
        elif graph[i][j] == 'B':
            DFS(i, j, 'B')
            answer[1] += cnt * cnt
print(*answer)
'''
answer = [0, 0]
for i in range(m):
    for j in range(n):
        cnt = 0
        if graph[i][j] == 'W':
            answer[0] += BFS(i, j)
        elif graph[i][j] == 'B':
            answer[1] += BFS(i, j)
print(*answer)
