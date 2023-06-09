# Q 35. 못생긴 수 (DP)
# Google 인터뷰 문제
'''
못생긴 수: 오직 2, 3, 5를 약수로 가지는 합성수
1이 못생긴 수일 때 n번째 못생긴 수를 출력하라
1 ≤ n ≤ 1,000
0번째 못생긴 수 = 1
1 * 2 = 2
1 * 3 = 3
1 * 5 = 5
1번째 못생긴 수 = 2 ((2, 3, 5)중 최소값)
2 * 2 = 4
1 * 3 = 3
1 * 5 = 5
3번째 못생긴 수 = 3 ((4, 3, 5)중 최소값)
2 * 2 = 4
2 * 3 = 6
1 * 5 = 5
4번째 못생긴 수 = 4 ((4, 6, 5)중 최소값)
4 * 2 = 8
2 * 3 = 6
1 * 5 = 5
{1, 2, 3, 4, 5, 6, 8, 9, 10, ...}
'''
n = int(input())
INF = int(1e9)
dp = [0] * n
dp[0] = 1

i2 = i3 = i5 = 0 # 2배, 3배, 5배 수를 구하기 위한 인덱스
# 처음 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    dp[l] = min(next2, next3, next5)
    if dp[l] == next2:
        i2 += 1
        next2 = dp[i2] * 2 # 2*2, 3*2, 4*2, 5*2 ...
    if dp[l] == next3:
        i3 += 1
        next3 = dp[i3] * 3 # 2*3, 3*3, 4*3, 5*3 ...
    if dp[l] == next5:
        i5 += 1
        next5 = dp[i5] * 5 # 2*5, 3*5, 4*5, 5*5 ...

print(dp[-1])