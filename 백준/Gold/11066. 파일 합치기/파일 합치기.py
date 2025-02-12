import sys

def min_merge_cost(K, files):
    # 누적합 계산
    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]
    
    # DP 테이블 초기화
    dp = [[0] * K for _ in range(K)]
    
    # 간격 2부터 K까지 탐색
    for length in range(2, K + 1):  # 파일 길이
        for i in range(K - length + 1):
            j = i + length - 1  # 끝점
            dp[i][j] = float('inf')
            
            # 최적의 분할점 k 찾기
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (prefix_sum[j + 1] - prefix_sum[i])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][K - 1]

# 입력 처리
T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    print(min_merge_cost(K, files))