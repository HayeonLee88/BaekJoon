# Q31. 금광 (DP)
'''
오른쪽 위: (-1, 1) -> (1, 1)
오른쪽 아래: (1, 1) -> (1, -1)
오른쪽: (0, 1) -> (1, 0)
열의 처음과 끝 위치에서는 2가지 경우의 수
1<= n, m <= 20
'''
import sys
T = int(input())
for test_case in range(T):
    n, m = sys.stdin.readline().rstrip().split()
    n, m = int(n), int(m)
    graph = []
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):
        graph.append(data[i * m : i * m + m])

    for i in range(1, m):
        M = -1
        for j in range(0, n):
            if j == 0:
                left_up = 0
            else:
                left_up = graph[j - 1][i - 1]
            if j == n - 1:
                left_down = 0
            else:
                left_down = graph[j + 1][i - 1]
            left = graph[j][i - 1]
            graph[j][i] = max(left_up, left, left_down) + graph[j][i]

    result = 0
    for i in range(n):
        result = max(result, graph[i][m - 1])
    print(result)
'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''