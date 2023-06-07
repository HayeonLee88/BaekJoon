# 15990번: 1, 2, 3 더하기 5
T = int(input())
# 1, 2, 3으로 끝나는 합의 개수
data = [[0, 0, 0, 0],
        [0, 1, 0, 0],  # 1은 1로 끝나는 합의 개수 한 개
        [0, 0, 1, 0],  # 2는 2로 끝나는 합의 개수 한 개
        [0, 1, 1, 1]]  # 3(21, 12, 3)은 1, 2, 3으로 끝나는 합의 개수 각 한 개씩
for i in range(4, 100001):
    data.append([0,
                 (data[i - 1][2] + data[i - 1][3]) % 1000000009,  # i보다 1 작은 수의 2와 3으로 끝나는 합의 개수
                 (data[i - 2][1] + data[i - 2][3]) % 1000000009,  # i보다 2 작은 수의 1와 3으로 끝나는 합의 개수
                 (data[i - 3][1] + data[i - 3][2]) % 1000000009])  # i보다 3 작은 수의 1와 2으로 끝나는 합의 개수
for test_case in range(T):
    n = int(input())
    print(sum(data[n]) % 1000000009)
