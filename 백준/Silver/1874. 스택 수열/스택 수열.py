import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = deque() # 수열을 만들 때 사용하는 스택
answer = [] # 수열을 만들 때의 연산을 저장하는 변수
end = 0 # stack에 append한 제일 큰 수

for i in range(n):
    num = int(input())
    if end < num:
        for i in range(end + 1, num + 1):
            stack.append(i)
            answer.append('+')
        stack.pop()
        answer.append('-')
        end = num
    elif end > num:
        if stack.pop() != num:
            answer = ["NO"]
            break
        else:
            answer.append('-')
    else:
        stack.pop()
        answer.append('-')

print(*answer, sep="\n")
