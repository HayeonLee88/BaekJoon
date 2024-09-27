import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    country = []
    p_cnt = 0
    union = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        now = graph[x][y]
        p_cnt += now
        union += 1
        country.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            nxt = graph[nx][ny]
            if l <= max(nxt, now) - min(nxt, now) <= r:
                q.append((nx, ny))
                visited[nx][ny] = True
    if union > 1:
        new = p_cnt // union
        for x, y in country:
            graph[x][y] = new
        return True

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if BFS(i, j):
                    check += 1
    if check == 0:
        break
    answer += 1
    
print(answer)