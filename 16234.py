# 16234번: 인구 이동
'''
NxN 땅
r행 c열에 A[r][c]명이 살고 있다.
인접한 나라 사이에는 국경선 존재.
    - 국경선 공유하는 두 나라 인구 차이가 L명 이상 R명 이하 => 하루 동안 국경선 열기
    - 위의 조건에 의해 국경선이 모두 열리면 인구 이동 시작
    - 인접한 칸만 이동할 수 있다면 그 나라를 오늘 하루 동안 연합이라 함
    - 연합을 이룬 각 칸의 인구수 = (연합의 인구수) // (연합을 이룬 칸의 수)
    - 연합을 해체하고 모든 국경선 닫기.
입력
N L R (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
N개의 줄에 각 나라의 인구수가 주어짐 (0 ≤ A[r][c] ≤ 100)

problem? 이때 인구 이동이 며칠 동안 발생하는지 출력하라
너비 우선 탐색
1행 1열부터 탐색 > 상하좌우 인접 칸과의 인구수 비교하여 조건에 맞으면 국경선 열기
국경선 열기 => 칸 정보 담기 & 인구 수 더하기 & 연합 수 더하기
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    country = [] # 연합 지역들의 위치를 담는 리스트
    p_cnt = 0 # 연합 내의 총 인구 수
    union = 0 # 연합의 수
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        now = graph[x][y]
        p_cnt += now
        union += 1
        country.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            nxt = graph[nx][ny]
            if l <= max(nxt, now) - min(nxt, now) <= r: # 인접 지역 간의 인구 차이가 l이상 r이하 라면
                q.append((nx, ny))
                visited[nx][ny] = True

    if union > 1: # 연합이 생겼다면
        new = p_cnt // union # 인구 이동을 마친 인원 수
        for x, y in country: # 연합인 지역들의 인구 수 변화
            graph[x][y] = new
        return True

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: # 방문한 지역이 아닐 경우
                if BFS(i, j): # 연합이 이뤄졌을 때
                    check += 1
    if check == 0: # 하루 동안 연합이 이뤄지지 않았다면
        break
    answer += 1

print(answer)
