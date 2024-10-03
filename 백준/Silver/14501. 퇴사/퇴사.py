n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    T, P = data[i]
    if i + T > n: # 마지막 날까지 일을 마칠 수 없다면
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(P + dp[i + T], dp[i + 1])

print(dp[0])