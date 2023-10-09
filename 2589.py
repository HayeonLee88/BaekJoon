# 2589번: 보물섬 (BFS, BruteForce)
'''
첫째 줄: 보물 지도의 세로의 크기와 가로의 크기 (50이하)
이어 L과 W로 표시된 보물 지도가 주어진다.
보물은 두 지점 사이의 최단거리가 가장 긴 곳에 묻혀있다.

problem: 첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력

How?
    보물이 묻혀있을 거라 생각되는 모든 'L'을 탐색하여 그 지점으로부처 BFS로 모든 땅과의 최단 거리를 구한다.
    이때 최단 거리가 가장 긴 곳이 보물이 묻힌 장소.
'''
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(pos_x, pos_y):
    count = 0
    q = deque()
    q.append((pos_x, pos_y, count)) # 위치와 최단거리를 담는다
    visited[pos_x][pos_y] = 0
    while q:
        now = q.popleft()
        for i in range(4): # 상/하/좌/우 움직이기
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            # 섬을 벗어나거나, 땅이 아니거나, 최단거리가 아닐 경우 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 'W' or visited[nx][ny] <= now[2] + 1:
                continue
            cnt = now[2] + 1 # 상/하/좌/우 움직이기 전 위치에서의 최단거리 + 1
            visited[nx][ny] = cnt # 최단 거리 초기화
            count = cnt # 제일 긴 최단 거리 담기
            q.append((nx, ny, cnt))
    return count

answer = [] # 한 지점으로부터 모든 최단거리 중 가장 긴 거리를 담는 리스트
INF = int(1e9)
for i in range(n): # 섬의모든 지점 탐색
    for j in range(m):
        visited = [[INF] * m for _ in range(n)] # 최단거리 리스트 초기화
        if graph[i][j] == 'L': # 탐색 지점이 땅일 때만
            answer.append(BFS(i, j))
print(max(answer))