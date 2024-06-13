import sys

INF = int(1e9)

def DP(graph, n):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0] = [INF, graph[0][1], graph[0][1] + graph[0][2]]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][2], dp[i][1]) + graph[i][2]
    return dp[-1][1]

input = lambda: sys.stdin.readline().rstrip()

k = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(f'{k}. {DP(graph, n)}')
    k += 1