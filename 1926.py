# 1926번: 그림 (그래프, BFS, DFS)
'''
그림이라는 것은 1로 연결된 것을 한 그림이라고 정의
n: 도화지의 세로 크기 (1 ≤ n ≤ 500)
m: 가로 크기 (1 ≤ m ≤ 500)
0/1:색칠이 안된/색칠이 된 부분

problem: 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

How?
    넓이 우선 탐색(그림 넓이 탐색):
    1. 종이 전체를 탐색할 때, 각 칸이 색칠되었고, 방문하지 않은 곳이라면 넓이 우선 탐색을 시작한다.
    2. 처음 칸에서 상하좌우로 음직이며 종이를 벗어나지 않고, 색칠이 된, 방문하지 않은 곳을 deque에 추가한다.
    3. 계속 움직이다 deque이 비면 탐색을 멈추가 그림의 넓이 cnt를 리턴한다.

    종이 전체를 탐색하여 각 칸이 색칠되었고, 방문하지 않은 곳이라면 그림 개수 + 1
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    cnt = 1 # 그림의 넓이
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 종이를 벗어나거나, 빈곳이거나, 이미 방문했다면 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= m or not graph[nx][ny] or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
            cnt += 1 # 넓이 + 1

    return cnt

count = 0
area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            a = bfs(i, j)
            area = max(area, a)
            count += 1

print(f'{count}\n{area}')