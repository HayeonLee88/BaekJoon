import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
sorted_students = [[] for _ in range(n * n + 1)]

for a, b, c, d, e in students:
    sorted_students[a] = [b, c, d, e]

graph = [[0] * n for _ in range(n)]
empty = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i in [0, n-1] and j in [0, n-1]:
            empty[i][j] = 2
        elif i in [0, n-1] or j in [0, n-1]:
            empty[i][j] = 3
        else:
            empty[i][j] = 4

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_first(a, b, c, d, e):
    global n
    tmp = []
    max_cnt = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            if graph[x][y]:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0<= ny < n:
                    if graph[nx][ny] in [b, c, d, e]:
                        cnt += 1
            if max_cnt < cnt:
                tmp = [[x, y]]
                max_cnt = cnt
            elif max_cnt == cnt:
                tmp.append([x, y])
    return tmp


def check_second(list_):
    answer = []
    empty_cnt = 0
    for x, y in list_:
        if empty_cnt < empty[x][y]:
            answer = [[x, y]]
            empty_cnt = empty[x][y]
        elif empty_cnt == empty[x][y]:
            answer.append([x, y])
    return answer


def check_third(list_):
    row = n
    col = n
    for x, y in list_:
        if row > x:
            row, col = x, y
        elif row == x:
            if col > y:
                col = y
    return [row, col]


for student in students:
    spaces = check_first(*student)
    if len(spaces) > 1:
        empty_space = check_second(spaces)
        if len(empty_space) > 1:
            x, y = check_third(empty_space)
        else:
            x, y = empty_space[0]
    else:
        x, y = spaces[0]

    graph[x][y] = student[0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n:
            empty[nx][ny] -= 1

answer = 0
for x in range(n):
    for y in range(n):
        cnt = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n:
                if graph[nx][ny] in sorted_students[graph[x][y]]:
                    cnt += 1
        if cnt != -1:
            answer += 10 ** cnt

print(answer)
