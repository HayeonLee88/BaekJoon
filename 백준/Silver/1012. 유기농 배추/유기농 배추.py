import sys

input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(100001)

t = int(input())


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y]: # 배추가 심어져 있다면
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

answer = []
for _ in range(t):
    tmp = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]


    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                tmp += 1
    answer.append(tmp)

print(*answer, sep='\n')