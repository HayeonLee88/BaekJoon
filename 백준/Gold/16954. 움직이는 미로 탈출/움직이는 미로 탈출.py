import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()
walls = deque()
graph = []

for i in range(8):
    graph.append(list(input()))
    for j in range(8):
        if graph[i][j] == '#':
            walls.append([i, j])

dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]

def BFS():
    q = deque()
    q.append((7, 0))
    while q:
        len_ = len(q)
        for i in range(len_):
            x, y = q.popleft()
            if [x, y] == [0, 7]:
                return 1

            if [x, y] in walls:
                continue
            for j in range(9):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx < 0 or nx > 7 or ny < 0 or ny > 7:
                    continue
                if [nx, ny] in walls:
                    continue
                q.append((nx, ny))
        len_ = len(walls)
        for i in range(len_):
            r, c = walls.popleft()
            if r + 1 > 7:
                continue
            walls.append([r + 1, c])
    return 0

print(BFS())