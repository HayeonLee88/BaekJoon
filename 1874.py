# 1874번: 스택수열

import sys
input = lambda :sys.stdin.readline().rstrip()
n = int(input())
answer = []
data = []
now, nxt, push, pop = 0, 0, 0, 0
for i in range(n):
    num = int(input())
    nxt = num
    if push == n:
        if now > nxt:
            data.pop()
            answer.append('-')
        else:
            break
    else:
        if nxt in data[-1:]:
            pop = nxt
            answer.append('-')
            data.pop()
        elif nxt > now:
            for j in range(nxt - push):
                data.append(push + j + 1)
                answer.append('+')
            data.pop()
            push = pop = nxt
            answer.append('-')
        else:
            break
    now = nxt
if len(answer) == 2 * n:
    for a in answer:
        print(a)
else:
    print('NO')
