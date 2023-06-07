# 14502번: 연구소
'''
연구소 크기 = NxM
바이러스 상하좌우 인접한 빈칸으로 이동.
새로 세울 벽의 개수: 3
꼭 3개를 세워야 함.
problem: 벽을 세운 뒤 바이러스가 퍼질 수 없는 안전 영역 크기의 최댓값을 구하라
3 ≤ N, M ≤ 8
0: 빈 칸 3개 이상
1: 벽
2: 바이러스 2 이상 10 이하
빈칸 최대 수 = 8*8 - 2 = 62
칸을 세울 조합: 62C3 = 대략 38,000
칸을 세운 후 안전영역 계산: BFS
모든 경우의 수 체크 Brute Force
'''
import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []  # 연구소 리스트

virus = []  # 바이러스 좌표
empty = []  # 빈 칸 좌표
empty_cnt = 0  # 빈 칸 수
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(row)
    for j in range(m):
        x = row[j]
        if x == 2:  # 바이러스가 있을 때
            virus.append((i, j))
        elif x == 0:  # 빈 칸일 때
            empty.append((i, j))
            empty_cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):  # 바이러스가 퍼지는 것을 넓이 우선 탐색으로 구현
    global cnt
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4): # 상하좌우 인접 칸 검사
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 연구소 내부일 때
                if tmp_graph[nx][ny] == 0:  # 빈 칸이라면
                    tmp_graph[nx][ny] = 2
                    q.append((nx, ny))
                    cnt -= 1  # 빈 칸 수에서 1빼기


# 빈 칸 좌표 리스트에서 3개를 뽑아 벽을 세울 공간을 정한다.
b_walls = list(combinations(empty, 3))

answer = 0  # 안전 영역
for a, b, c in b_walls:  # 벽을 세울 모든 경우의 수
    tmp_graph = copy.deepcopy(graph)
    # 벽 3개 세우기
    tmp_graph[a[0]][a[1]] = 1
    tmp_graph[b[0]][b[1]] = 1
    tmp_graph[c[0]][c[1]] = 1
    cnt = empty_cnt - 3  # 빈 칸의 수에서 새로 세운 벽 3개 빼기
    for x, y in virus:  # 바이러스가 있는 모든 위치에서 넓이 우선 탐색 시작
        bfs(x, y)
    answer = max(answer, cnt)  # 최대 안전 영역 구하기

print(answer)
