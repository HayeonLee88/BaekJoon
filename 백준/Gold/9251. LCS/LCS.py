s1 = " " + input()
s2 = " " + input()

n1, n2 = len(s1), len(s2)

dp = [[0] * n2 for _ in range(n1)]

for i in range(1, n1):
    for j in range(1, n2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n1 - 1][n2 - 1])