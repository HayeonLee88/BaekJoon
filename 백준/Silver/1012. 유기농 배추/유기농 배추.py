import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(30001)
def DFS(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[x][y]:
        graph[x][y] = 0
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True
    return False

T = int(input())
for test_case in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    answer = 0
    for i in range(m):
        for j in range(n):
            if DFS(i, j):
                answer += 1

    print(answer)