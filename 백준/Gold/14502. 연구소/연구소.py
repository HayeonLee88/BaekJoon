import sys
from collections import deque
from itertools import combinations

input = lambda:sys.stdin.readline().rstrip()

graph = [] # 연구소의 지도를 담는 리스트
viruses = [] # 바이러스의 위치를 담는 리시트
empty = [] # 빈 칸의 위치를 담는 리스트

n, m = map(int, input().split())
total = -3 # 빈 칸의 총 수

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        x = graph[i][j]
        if x == 2:
            viruses.append([i, j])
        elif x == 0:
            total += 1
            empty.append([i, j])

# 새로 새울 3개의 벽의 조합
walls = list(combinations(empty, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global total, viruses
    cnt = 0
    q = deque()
    for virus in viruses:
        q.append(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # map을 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 빈 칸이면서 바이러스가 퍼지지 않은 경우
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True
                cnt += 1
    return total - cnt

answer = 0
for a, b, c in walls:
    visited = [[False] * m for _ in range(n)]
    # 새로운 벽 세우기
    graph[a[0]][a[1]] = 1
    graph[b[0]][b[1]] = 1
    graph[c[0]][c[1]] = 1
    
    # 최대 안전 영역 구하기
    answer = max(answer, bfs())
   
    graph[a[0]][a[1]] = 0
    graph[b[0]][b[1]] = 0
    graph[c[0]][c[1]] = 0

print(answer)