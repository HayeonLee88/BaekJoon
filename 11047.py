# 11047번: 동전 0 / 그리디
n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
answer = 0
for i in range(-1, -n - 1, -1):
    coin = coins[i]
    if coin <= k:
        answer += k // coin
        k %= coin

print(answer)
