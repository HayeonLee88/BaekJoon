import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = []
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        now_cnt = visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            next_cnt = visited[nx][ny]
            wall_or_room = graph[nx][ny]
            if next_cnt == -1 or next_cnt > now_cnt + wall_or_room:
                visited[nx][ny] = now_cnt + wall_or_room
                if nx == n-1 and ny == m-1:
                    continue
                q.append((nx, ny))
    return visited[n-1][m-1]

print(BFS(0, 0))