import sys

input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(m + 1)]

info = [[0, 0]]
for _ in range(m):
    info.append(list(map(int, input().split())))

for i in range(1, m + 1):
    for j in range(1, n + 1):
        now = info[i][0]
        if now <= j:
            dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - now] + info[i][1]))
        elif now > j:
            dp[i][j] = dp[i - 1][j]

print(dp[m][n])