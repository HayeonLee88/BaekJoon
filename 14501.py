# 14501번: 퇴사 (DP)
'''
1 ≤ N ≤ 15
N일 동안 상담을 할 때 받을 수 있는 최대 수익을 구하라.
Ti = 상담이 걸리는 시간 (1 ≤ Ti ≤ 5)
Pi = 상담 수익 (1 ≤ Pi ≤ 1,000)
마지막 N일 부터 역으로 계산하기
'''
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    T, P = data[i]
    if i + T > n: # 마지막 날까지 일을 마칠 수 없다면
        dp[i] = dp[i + 1] # i+1일 값 그대로 가져오기
    else: # 현재 상담 수익 + (현재 상담 끝나는 날 + 1)일 수익과 i+1일 값 비교하기
        dp[i] = max(P + dp[i + T], dp[i + 1])
print(dp[0])