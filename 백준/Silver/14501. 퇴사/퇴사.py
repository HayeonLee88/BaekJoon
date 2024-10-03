import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
counsel = [list(map(int, input().split())) for _ in range(n)]

stack = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if n - i >= counsel[i][0]:
        tmp = counsel[i][1] + stack[i + counsel[i][0]]
        if tmp > stack[i + 1]:
            stack[i] = tmp
        else:
            stack[i] = stack[i + 1]

    else:
        stack[i] = stack[i + 1]

print(stack[0])