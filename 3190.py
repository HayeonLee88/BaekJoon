# 3190번: 뱀(Deque, Queue)

'''
NxN 정사각 보드, 몇몇 칸에는 사과가 놓여있다
시작할때 뱀은 맨위 맨좌측에 위치, 처음에 오른쪽을 향한다
X C: X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.

problem? 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라

How?
    (n + 1) * (n + 1)칸을 만들기
    사과가 있는 곳은 1, 빈칸은 0
    dx, dy: C에 따른 방향 변화
    h: 뱀의 머리 위치, 방향
    body: 뱀의 몸의 위치를 담는 queue
    pos: {숫자(keys): (dx, dy)(values)} 시계 방향에에 따른 움직임을 담는 딕셔너리
    D: 뱀의 방향 전환 정보를 담는 queue (X, C)
    d: 뱀의 머리 방향 (0, 1, 2, 3)

    1. 뱀의 머리 방향에 따른 pos[d]와 현재 x, y위치를 더해 다음 머리의 위치 구하기
    2. 뱀의 머리가 1.벽이나 몸에 닿는다면 종료
                 2. 빈칸이라면 body popleft
                 3. 사과라면 보드 위 사과 지우기
                 2, 3의 경우 머리 위치 body에 저장
    3. 현재 시간과 뱀의 방향 전환 정보가 일치하면 D popleft
    4. 왼쪽 회전이면 d -= 1, 오른쪽 회전이면 d += 1
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(int(input())):
    x, y = map(int, input().split())
    board[x][y] = 1 # 사과가 있는 곳은 1

L = int(input()) # 방향 전환 횟수
D = deque(list(input().split()) for _ in range(L)) # 방향 전환 정보 큐

body = deque() # 뱀의 몸의 위치를 저장하는 큐 초기화
body.append((1, 1)) # 뱀의 처음 위치 저장
h = [1, 1] # 뱀의 머리 위치 초기화

pos = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} # 시계방향: 동, 남, 서, 북
d = 0 # 뱀의 머리 방향

INF = int(1e9)
for i in range(1, INF):
    x, y = h
    dx, dy = pos[d]
    nx, ny = x + dx, y + dy

    if nx == 0 or ny == 0 or nx > n or ny > n or (nx, ny) in body: # 벽이나 자신의 몸과 부딪히면 종료
        break

    n_pos = board[nx][ny]
    if n_pos == 0: # 사과가 없다면
        body.popleft() # 꼬리 줄어들기
    else:
        board[nx][ny] = 0
    body.append((nx, ny)) # 움직인 머리의 위치 저장

    h = [nx, ny] # 머리 위치 초기화

    if D and int(D[0][0]) == i: # 방향 회전을 한다면
        time, ctrl = D.popleft()
        if ctrl == 'L': # 왼쪽 90도
            d = (d - 1) % 4
        else: # 오른쪽 90도
            d = (d + 1) % 4

print(i)
