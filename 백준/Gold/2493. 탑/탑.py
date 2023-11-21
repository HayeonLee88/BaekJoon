import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tops = list(map(int, input().split()))

answer = []
highest = [[0, 0]] # i번째의 탑에서 가장 가까운 [제일 높은 탑의 위치, 높이]를 담는 스택

for i in range(n):
    top = tops[i]
    while highest and top > highest[-1][-1]:
        highest.pop()
    if highest:
        answer.append(highest[-1][0])
    else:
        answer.append(0)
    highest.append([i + 1, top])

print(*answer)
