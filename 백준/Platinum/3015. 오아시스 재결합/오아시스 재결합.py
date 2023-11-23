import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
line = [int(input()) for _ in range(n)]
stack = []
answer = 0
for i in range(n):
    now = line[i]
    cnt_same_num = 1
    while stack and now >= stack[-1][0]:
        num, cnt = stack.pop()
        answer += cnt
        if num == now:
            cnt_same_num += cnt
    if stack:
        answer += 1
    stack.append([now, cnt_same_num])

print(answer)
