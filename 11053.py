# 11053번: 가장 긴 증가하는 부분 수열 (DP)
'''
문제
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
'''
n = int(input())
data = list(map(int, input().split()))
DP = [1] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            DP[i] = max(DP[i], DP[j] + 1)
print(DP)
print(max(DP))