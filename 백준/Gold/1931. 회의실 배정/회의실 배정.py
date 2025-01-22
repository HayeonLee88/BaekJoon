import sys


input = lambda:sys.stdin.readline().rstrip()

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting.sort()
meeting.sort(key=lambda x: x[1])

answer = 1
prev = meeting[0][1]
for i in range(1, n):
    start, end = meeting[i]
    if prev > start:
        continue
    answer += 1
    prev = end

print(answer)