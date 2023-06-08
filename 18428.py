# 18428번: 감시 피하기
'''
NxN 크기의 복도
각 칸에는 선생님(T), 학생(S), 장애물(O)이 위치할 수 있음
빈 칸 = X
각 칸의 선생님 상, 하, 좌, 우 방향 감시 => 장애물에 가로 막히지 않은 복도 모두 볼 수 있음
    체스 퀸?
problem: 복도의 빈 칸에 장애물 3개를 설치하여
        모든 학생이 감시를 피할 수 있는지 확인 > 피할 수 있다면 'YES', 없다면 'NO'
입력:  N (3 ≤ N ≤ 6), 2~N+1줄 복도 정보
1 ≤ T ≤ 5, 1 ≤ S ≤ 30
brute force
(i, j)
(i, 0) ~ (i, n-1) & (0, j) ~ (n-1, j)
'''
from itertools import combinations
import sys

sys.setrecursionlimit(100000)
n = int(input())

hallway = []
teachers = []
students = []
empty = []
for i in range(n):
    row = list(input().split())
    hallway.append(row)
    for j in range(n):
        if row[j] == 'T':
            teachers.append((i, j))
        elif row[j] == 'S':
            students.append((i, j))
        else:
            empty.append((i, j))


def DFS(x, y, d):
    if x < 0 or x >= n or y < 0 or y >= n:  # 끝까지 왔다면 True
        return True
    if d == 0:
        if hallway[x][y] == 'S':  # 학생을 봤다면 False
            return False
        elif hallway[x][y] == 'O':  # 장애물이 나온다면 True
            return True
        else:
            return DFS(x - 1, y, d)  # 복도가 빈 칸일 동안 재귀적 수행
    elif d == 1:
        if hallway[x][y] == 'S':  # 학생을 봤다면 False
            return False
        elif hallway[x][y] == 'O':  # 장애물이 나온다면 True
            return True
        else:
            return DFS(x + 1, y, d)
    elif d == 2:
        if hallway[x][y] == 'S':  # 학생을 봤다면 False
            return False
        elif hallway[x][y] == 'O':  # 장애물이 나온다면 True
            return True
        else:
            return DFS(x, y - 1, d)
    else:
        if hallway[x][y] == 'S':  # 학생을 봤다면 False
            return False
        elif hallway[x][y] == 'O':  # 장애물이 나온다면 True
            return True
        else:
            return DFS(x, y + 1, d)


obstacles = list(combinations(empty, 3))
for a, b, c in obstacles:
    answer = True
    # 장애물 세우기
    hallway[a[0]][a[1]] = 'O'
    hallway[b[0]][b[1]] = 'O'
    hallway[c[0]][c[1]] = 'O'
    for x, y in teachers:
        # 상, 하, 좌, 우 탐색 후 학생이 발견됐을 때
        if not DFS(x - 1, y, 0) or not DFS(x + 1, y, 1) or not DFS(x, y - 1, 2) or not DFS(x, y + 1, 3):
            answer = False
            break
    # 모든 선생님이 감시 후 학생르 발견 못했다면
    if answer:
        break
    # 장애물 치우기
    hallway[a[0]][a[1]] = 'X'
    hallway[b[0]][b[1]] = 'X'
    hallway[c[0]][c[1]] = 'X'

print('YES' if answer else 'NO')
