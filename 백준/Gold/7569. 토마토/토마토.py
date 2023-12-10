import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

m, n, h = map(int, input().split())
graph = []

riped_tomatoes = deque()
for i in range(h):
    temp = []
    for j in range(n):
        row = list(map(int, input().split()))
        temp.append(row)
        for k in range(m):
            if row[k] == 1:
                riped_tomatoes.append((i, j, k))
    graph.append(temp)

dic = {0: [1, 0, 0], 1: [-1, 0, 0], 2: [0, 1, 0],  # 0:앞, 1:뒤, 2:위
       3: [0, -1, 0], 4: [0, 0, 1], 5: [0, 0, -1]}  # 3: 아래, 4: 오른쪽, 5: 왼쪽

def bfs(t, r, c):
    ck = False
    for i in range(6):
        dt, dr, dc = dic[i]
        nt = t + dt
        nr = r + dr
        nc = c + dc
        if nt < 0 or nt >= h or nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if graph[nt][nr][nc] == 0:
            riped_tomatoes.append((nt, nr, nc))
            graph[nt][nr][nc] = 1
            ck = True

    return ck

answer = 0
while riped_tomatoes:
    check = False
    length = len(riped_tomatoes)
    for _ in range(length):
        a, b, c = riped_tomatoes.popleft()
        if bfs(a, b, c):
            check = True
    if not check:
        break
    answer += 1

for array in graph:
    for row in array:
        for x in row:
            if x == 0: # 안익은 토마토가 있다면
                answer = -1
                break
        if answer == -1:
            break
    if answer == -1:
        break
print(answer)