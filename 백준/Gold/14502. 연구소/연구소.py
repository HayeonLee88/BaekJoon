import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []

virus = []
empty = []
empty_cnt = 0
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(row)
    for j in range(m):
        x = row[j]
        if x == 2:
            virus.append((i, j))
        elif x == 0:
            empty.append((i, j))
            empty_cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx, ny))
                    cnt -= 1

b_walls = list(combinations(empty, 3))

answer = 0
for a, b, c in b_walls:
    tmp_graph = copy.deepcopy(graph)
    tmp_graph[a[0]][a[1]] = 1 # 벽 세우기
    tmp_graph[b[0]][b[1]] = 1
    tmp_graph[c[0]][c[1]] = 1
    cnt = empty_cnt - 3 # 새로 새운 벽 3개 빼기
    for x, y in virus:
        bfs(x, y)
    answer = max(answer, cnt)

print(answer)