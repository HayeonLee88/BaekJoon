import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
line = [int(input()) for _ in range(n)]
stack = []
answer = 0
for i in range(n):
    now = line[i]
    cnt_same_num = 1
    while stack:
        if stack[-1][0] < now:
            _, cnt = stack.pop()
            answer += cnt
        elif stack[-1][0] == now:
            _, cnt = stack.pop()
            cnt_same_num += cnt
            answer += cnt
        else:
            answer += 1
            break
    stack.append([now, cnt_same_num])

print(answer)
