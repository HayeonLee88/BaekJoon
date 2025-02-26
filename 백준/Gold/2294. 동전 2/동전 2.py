import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = list({int(input()) for _ in range(n)})
coins.sort()

INF = int(1e9)
dp = [INF] * (k + 1)

for coin in coins:
    if coin > k:
        break
    dp[coin] = 1

# 동전 한 가지 종류를 이용해 만드는 동전 개수 저장
for i in range(1, k + 1):
    tmp = 0
    for coin in coins:
        tmp = i + coin # 2 + 1
        if tmp > k:
            break
        dp[tmp] = min(dp[tmp], dp[i] + 1)
        
answer = dp[-1]
print(answer if answer != INF else -1)