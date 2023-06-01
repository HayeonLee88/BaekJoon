# 2468 안전영역 DFS

import sys

sys.setrecursionlimit(40001)
input = lambda :sys.stdin.readline().rstrip()
n = int(input())
data = []
max_h = 0

for i in range(n):
    cities = list(map(int, input().split()))
    data.append(cities)
    cities.append(max_h)
    max_h = max(cities)

def dfs(x, y, k):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if not graph[x][y] and data[x][y] > k:
        graph[x][y] = True
        dfs(x-1, y, k)
        dfs(x+1, y, k)
        dfs(x, y-1, k)
        dfs(x, y+1, k)
        return True
    return False

answer = 0
for k in range(0, max_h):
    graph = [[False]*n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, k):
                tmp += 1
    answer = max(answer, tmp)
print(answer)


