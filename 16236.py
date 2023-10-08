# 16236번: 아기 상어
'''
1:08~47
NxN 크기의 공간에 물고리 M마리와 아기 상어 1마리.
아기 상어의 처음 크기는 2, 1초에 상하좌우로 인접한 한 칸씩 이동한다.
자신보다 큰 물고기가 있는 칸은 지날 수 없고, 나머지 칸은 지날 수 있음.
자신보다 작은 물고기만 먹을 수 있다.
크기가 같은 물고기는 먹을 수 없지만 그 칸을 지나갈 수 있다.

- 더 이상 먹을 물고기가 공간에 없다면 도움 요청
- 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 감
- 먹을 수 있는 물고기가 1마리가 넘는다면 거리가 가장 가까운 물고기를 먹으러 감
    - 지나야하는 칸의 개수의 최솟값
    - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그런 물고기가 여러 마리라면. 가장 왼쪽 물고기를 먹는다.

아기 상어 이동 시간 1초. 자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가.
아기 상어가 몇 초 동안 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하라.

공간의 크기 N(2 ≤ N ≤ 20)
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치

거리 구하기 = abs(아기 상어 행 - 물고기 행) + abs(아기 상어 열 - 물고기 열)
상어보다 크기가 큰 물고기는 피해서 가야함. 위의 거리 구하기로 구할 수 X
넓이 우선 탐색
시작 후 크기가 1인 물고기가 없다면 종료
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)
n = int(input())
graph = []
info = []
x, y = 0, 0
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for index, k in enumerate(row):
        info.append([k, i, index])

info.sort(key=lambda data: data[0]) # 크기 순으로 정렬

start_x, start_y = info[-1][1:]
shark = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
row = [INF] * n
visited = [row for _ in range(n)]

def BFS():
    q = deque()
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] > shark:
                continue
            if graph[nx][ny] == shark:

            else:

