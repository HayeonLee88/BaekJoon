# 2294번: 동전2(DP)
'''
동전의 가치는 100,000보다 작거나 같은 자연수, 가치가 같은 동전이 여러 번 주어질 수도 있다.
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원
그러면서 동전의 개수가 최소가 되도록 하려고 한다. n, k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)

problem: 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

How?
    dp: 다이나믹 프로그래밍 값을 담는 리스트, 리스트의 값을 INF(1e9)로 초기화 한다.

    1. 동전을 집합에 담아 반복되는 값을 없애고 리스트로 바꾼 후, 정렬한다.
    2. coins를 탐색하여 k값을 넘지 않을 때 dp의 값을 1로 초기화 한다.
    3. 1부터 k까지 탐색하며 모든 각 동전의 값과 더하고 그 값을 tmp에 담는다.
    4. tmp가 k를 넘지 않으면 dp[tmp]와 dp[현재동전] + 1을 비교하여 작은 값으로 변경한다.

'''
import sys

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
        tmp = i + coin # 동전을 두 개이상 사용하는 값
        if tmp > k:
            break
        dp[tmp] = min(dp[tmp], dp[i] + 1) # 이전의 개수와 새로 더한 개수를 비교하여 값을 변경한다.

answer = dp[-1] # k를 만드는 동전 최소 개수를 저장
print(answer if answer != INF else -1)