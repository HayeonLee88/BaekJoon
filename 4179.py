# 4179번: 불! (BFS)
'''
R = 미로 행의 개수, C = 열의 개수. (1 ≤ R, C ≤ 1000)

#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간

상하좌우로 퍼지는 불, 상/하/좌/우로 한 칸 움직이는 지훈
미로의 가장자리에 접한 공간에서 탈출할 수 있다.
벽이 있는 공간은 통과하지 못한다.

problem: 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
        지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
How?
    fire: 불이 확산되는 위치를 담는 덱
    jihoon: 지훈이의 위치를 담는 덱
    bfs(): 불의 확산과 지훈이의 이동 구현 함수, 이동 후 지훈이의 위치가 가장자리이면 True를 반환한다.

    넓이 우선 탐색을 통해 먼저 불이 확산하는 위치를 구한 후, 지훈이가 이동할 수 있는 위치를 구한다.
    이때 fire에 불이 확산되는 위치와 jihoon에 지훈이가 이동하는 위치를 담는다.
    bfs 실행 후 jihoon이 비었다면 지훈이가 더 이상 움직이 공간이 없음을 의미하므로 IMPOSSIBLE을 출력한다.
    만약 bfs 실행 후 True가 반환되었다면 탈출시간을 출력한다.
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

fire = deque()
jihoon = deque()

r, c = map(int, input().split())
graph = []
visited = [[False] * c for _ in range(r)]

cnt = r * c
for i in range(r):
    row = list(input())
    graph.append(row)
    for j in range(c):
        if row[j] == 'J':
            jihoon.append([i, j])
        elif row[j] == 'F':
            fire.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start, type):
    x, y = start
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        pos_x, pos_y = q.popleft()
        for i in range(4):
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny] or graph[nx][ny] == '#':
                continue
            visited[nx][ny] = True
            if type == 'F':
                graph[nx][ny] = 'F'
                fire.append([nx, ny])
            else:
                if graph[nx][ny] == 'F':  # 불이 있는 곳이면 이동하지 않는다.
                    continue
                elif nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
                    return True
                jihoon.append([nx, ny])  # 지훈이가 움직일 수 있는 위치 저장
    return False


answer = 1
x, y = jihoon[0]
# 만약 지훈이의 시작위치가 가장자리라면
if x == 0 or x == r - 1 or y == 0 or y == c - 1:
    pass
else:
    while True:
        check = False
        for i in range(len(fire)):  # 불의 확산
            bfs(fire.popleft(), 'F')
        for i in range(len(jihoon)):  # 지훈이 이동
            check = bfs(jihoon.popleft(), 'J')
            if check:  # 지훈이가 가장자리로 이동했다면
                break

        answer += 1
        if check:  # 탈출
            break
        elif not jihoon:  # 지훈이가 더 이상 이동할 수 없다면
            answer = 'IMPOSSIBLE'
            break
print(answer)


'''
Examples

input:
4 4
J.##
####
####
#..F

output: 1

input
4 4
####
#JF#
#..#
#..#

output: 3
'''
