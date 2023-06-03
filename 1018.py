# 1018번: 체스판 다시 칠하기
import sys
n, m = map(int, input().split())
chess = [sys.stdin.readline().rstrip() for _ in range(n)]
line = ['WBWBWBWB', 'BWBWBWBW']

answer = 2000
for i in range(n - 7):
    for j in range(m - 7):
        w_first = 0
        b_first = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if chess[x][y] != line[(x - i) % 2][y - j]:
                    w_first += 1
                else:
                    b_first += 1
        answer = min(answer, w_first, b_first)
print(answer)