import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 제일 처음일 때 왼쪽 합은 0
            left = 0
        else:
            left = triangle[i][j] + triangle[i - 1][j - 1]
        if j == i: # 제일 끝일 때 오른쪽 합은 0
            right = 0
        else:
            right = triangle[i][j] + triangle[i - 1][j]
        triangle[i][j] = max(left, right)

print(max(triangle[-1])) # 마지막 줄의 최대값