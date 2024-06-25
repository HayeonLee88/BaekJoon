import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_fire(q, map, n, m):
    len_ = len(q)
    for _ in range(len_):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            if map[nx][ny] not in ["#", "*"]:
                map[nx][ny] = "*"
                q.append([nx, ny])

def move_sg(q, map, n, m):
    len_ = len(q)
    for _ in range(len_):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == 0 or nx == n + 1 or ny == 0 or ny == m + 1:
                return True
            if nx < 0 or nx > (n + 1) or ny < 0 or ny > (m + 1):
                continue
            if map[nx][ny] == ".":
                map[nx][ny] = "@"
                q.append([nx, ny])

for test_case in range(T):
    fires = deque()
    pos = deque()
    m, n = map(int, input().split())
    graph = [['.'] * (m + 2)]
    for i in range(1, n + 1):
        row = input()
        graph.append(['.'])
        for j in range(m):
            if row[j] == "@":
                pos.append([i, j + 1])
            elif row[j] == "*":
                fires.append([i, j + 1])
            graph[i].append(row[j])
        graph[i].append('.')
    graph.append([['.'] * (m + 2)])

    escape = False
    answer = 0
    while not escape:
        if not pos:
            answer = "IMPOSSIBLE"
            break
        move_fire(fires, graph, n, m)
        escape = move_sg(pos, graph, n, m)
        answer += 1
    print(answer)
