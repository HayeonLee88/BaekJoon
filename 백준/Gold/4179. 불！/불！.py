import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

fire = deque()
jihoon = deque()

r, c = map(int, input().split())
graph = []
visited = [[False] * c for _ in range(r)]

cnt = r * c
for i in range(r):
    row = list(input())
    graph.append(row)
    for j in range(c):
        if row[j] == 'J':
            jihoon.append([i, j])
        elif row[j] == 'F':
            fire.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start, type):
    x, y = start
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        pos_x, pos_y = q.popleft()
        for i in range(4):
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny] or graph[nx][ny] == '#':
                continue
            visited[nx][ny] = True
            if type == 'F':
                graph[nx][ny] = 'F'
                fire.append([nx, ny])
            else:
                if graph[nx][ny] == 'F': # 불이 있는 곳이면 이동하지 않는다.
                    continue
                elif nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
                    return True
                jihoon.append([nx, ny]) # 지훈이가 움직일 수 있는 위치 저장
    return False

answer = 1
x, y = jihoon[0]
if x == 0 or x == r - 1 or y == 0 or y == c - 1:
    pass
else:
    while True:
        check = False
        for i in range(len(fire)):
            bfs(fire.popleft(), 'F')
        for i in range(len(jihoon)):
            check = bfs(jihoon.popleft(), 'J')
            if check:
                break

        answer += 1
        if check:
            break
        elif not jihoon:
            answer = 'IMPOSSIBLE'
            break
print(answer)
