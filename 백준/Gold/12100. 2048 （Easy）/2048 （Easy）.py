import sys
sys.setrecursionlimit(1000000)
intput = lambda:sys.stdin.readline().rstrip()

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]
answer = 0

def check(board):
    max_ = 0
    for i in range(n):
        for j in range(n):
            max_ = max(max_, board[i][j])
    return max_
    
dir = {0: [0, n, 1], 1: [n - 1, -1, -1], 2: [0, n, 1], 3: [n - 1, -1, -1]}

def move_1(i, graph):
    start, end, step = dir[i]
    tmp = [[0] * n for _ in range(n)]
    for j in range(n):
        cnt = start
        prev = 0
        for i in range(start, end, step):
            now = graph[i][j]
            if now != 0:
                if prev == now:
                    tmp[cnt - step][j] = now * 2
                    prev = 0
                    continue
                tmp[cnt][j] = now
                cnt += step
                prev = now
    return tmp


def move_2(i, graph):
    start, end, step = dir[i]
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        cnt = start
        prev = 0
        for j in range(start, end, step):
            now = graph[i][j]
            if now:
                if prev == now:
                    tmp[i][cnt - step] = now * 2
                    prev = 0
                    continue
                tmp[i][cnt] = now
                cnt += step
                prev = now
    
    return tmp


def dfs(graph, cnt):
    global answer
    if cnt > 5:
        answer = max(answer, check(graph))
        return
    for dir in range(4):
        if dir < 2:
            tmp = move_1(dir, graph)
        else:
            tmp = move_2(dir, graph)

        dfs(tmp, cnt + 1)


dfs(board, 1)

print(answer)