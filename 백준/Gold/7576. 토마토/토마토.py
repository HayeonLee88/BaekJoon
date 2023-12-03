import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

m, n  = map(int, input().split())
graph = []
ripe_xy = []
cnt_wall = 0
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] == 1:
            ripe_xy.append((i, j))
        elif data[j] == -1:
            cnt_wall += 1
cnt_unripe = m * n - len(ripe_xy) - cnt_wall

# 상 하 좌 우 움직이기
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def BFS(xy_list):
    cnt = 0
    q = deque()
    for xy in xy_list:
        q.append(xy)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                cnt += 1
    if cnt == cnt_unripe:
        return graph[x][y]
    return 0

print(BFS(ripe_xy)-1)