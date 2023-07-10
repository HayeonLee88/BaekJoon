# 18353번: 병사 배치하기 (DP)
'''
무작위로 나열된 N명의 병사들 중 특정 위치에 있는 병사를 열외시켜 전투력이 높은 순으로 내림차순 배치하도록 한다.
이때 남아있는 병사의 수가 최대가 될 열외시키는 병사의 수를 출력하라
1 ≤ N ≤ 2,000
각 병사의 전투력은 10,000,000이하 자연수
'''
n = int(input())
data = list(map(int, input().split()))
data.reverse()
dp = [1] * n

for i in range(n):
    now = data[i]
    for j in range(i):
        if data[j] < now:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
'''
10
1 2 3 4 5 3 6 1 8 5
'''