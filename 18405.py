# 18405번: 경쟁적 전염
'''
NxN 크기의 시험관, 1칸은 1x1 크기
바이러스의 종류: 1~K번
모든 바이러스 1초마다 상, 하, 좌, 우로 증식
    -매 초마다 번호가 낮은 종류부터 증식함
    -이미 바이러스가 있는 칸이라면 다른 바이러스가 침투할 수 없다.
Problem: S초가 지난 후 (X, Y)에 존재하는 바이러스의 종류를 출력하시오
1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000
0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N
첫번째 줄 N K
2~n+1줄 ki x y
n+1줄   S X Y
S초 후 해당 위치에 바이러스가 없을 경우 0 출력
바이러스를 담는 리스트를 바이러스의 번호를 기준으로 정렬
S회 만큼 넓이 우선 탐색을 실시 하여 바이러스를 증식한다.
'''
import sys
from collections import deque
import heapq

n, k = map(int, input().split())
graph = []
viruses = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(row)
    for j in range(n):
        data = row[j]
        if data > 0:
            heapq.heappush(viruses, (data, i, j)) # 바이러스의 번호가 작은 순으로 정렬하기 위해 heapq 사용
s, x, y = map(int, sys.stdin.readline().rstrip().split())

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(v):
    q = deque()
    for _ in range(len(v)):
        q.append(heapq.heappop(v)) # 최소힙 q에 넣기
    while q:
        num, x, y = q.popleft() # 작은 번호부터 순서대로 꺼내기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나거나 이미 바이러스가 있을 때 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 0:
                continue
            heapq.heappush(v, (num, nx, ny)) # 새롭게 퍼질 바이러스를 heapq로 담기
            graph[nx][ny] = num # 해당 위치의 값을 바이러스로 바꾸기

for i in range(s): # S초 동안 증식하기
    BFS(viruses)
    if len(viruses) == 0: # 더이상 퍼질 바이러스가 없을 때 증식 멈추기
        break

print(graph[x-1][y-1])
