# 7569번: 토마토(BFS)
'''
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수, 쌓아올려지는 상자의 수를 나타내는 H
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다
익은 토마토의 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 안 익은 토마토가 영향을 받아 익는다.

problem: 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산하여 출력하기.
         만약 모든 토마토가 익어 있다면 0, 토마토가 모두 익지 못한다면 -1 출력

How? 익은 토마토를 덱에 담아 익은 토마토의 주변을 넓이 우선 탐색한다.
     이때 안익은 토마토가 인접해 있다면 이 토마토의 위치를 덱에 담고, 새로 익은 토마토가 있음을 체크한다.
     넓이 우선 탐색 함수는 새로 익은 토마토가 있으면 True, 없다면 False를 반환한다.

     덱의 모든 토마토를 탐색한 후, False이면 토마토가 모두 익는 최소 일수가 멈춘다.

     answer(최소 일수)는 새로 익는 토마토가 생긴다면 1 더하기, 최소 일수가 멈춘 후, 토마토 전체를 탐색하여 안익은 토마토가 있다면 -1

tips:
        1. 시간 초과: 안 익은 토마토를 덱에 담아 탐색
                    - 안 익은 토마토가 익는다면 ? 만약 당일 익은 토마토 주변에 안 익은 토마토가 있으면 이 토마토에 영향을 미친다.
                    - 위를 해결하기 위해 당일 익은 토마토를 다른 덱에 담아 안 익은 토마토를 모두 탐색한 후, 토마토를 1로 바꿔야한다.
                     이 과정에서 시간이 초과된다.
           해결 방법: 익은 토마토를 덱에 담아 탐색하기
                    - 새로 익은 토마토를 1로 변경하고, 위치를 덱에 이 토마토의 인접한 익지 않은 토마토에 영향을 미치지 않는다.
'''
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
            print(f'벗어낫음: {nt}, {nr}, {nc}')
            continue
        if graph[nt][nr][nc] == 0:
            print(f'새로 익은 토마토: {nt}, {nr}, {nc}')
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
