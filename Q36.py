# Q 36. 편집 거리 (DP)
# Goldman Sachs 인터뷰
'''
6:54~
1. 삽입: 특정 위치에 문자 삽입
2. 삭제: 특정 위치 문자 삭제
3. 교체: 특정 위치 문자를 다른 문자로 교체
두 문자열 A와 B. 각 문자열의 기리는 5,000이하의 자연수
문자열 A를 B로 만드는 최소 편집 거리를 계산하라.
문자열 A의 i번째 문자와 문자열 B의 j번째 문자가 일치하는지 확인
    > A의 i+1번쨰 문자가 문자열 j번째 이후의 문자와 일치하는지 확인
    > 반복
    answer = B의 길이 - 일치하는 문자가 최대가 되는 수
'''
a = input()
b = input()
n, m = len(a), len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
print(dp[n][m])
