# 1935번: 후위 표기식2 (Stack)
'''
첫째 줄 피연산자의 개수(1 ≤ N ≤ 26)
둘째 줄에는 후위 표기식
셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값 (100이하 자연수)
problem 계산 결과를 소숫점 둘째 자리까지 출력하기

1. 숫자는 스택에 담기
2-1. 연산자가 나오면 숫자 스택에서 2개 pop
2-2. 두번째 pop한 숫자가 첫번째 피연산자이다.
3. 이 두 수를 연산한 수를 다시 스택에 담는다.
'''
from collections import deque

n = int(input())
calc = input()
nums = [0] * 26
for i in range(n):
    nums[i] = int(input())

stack_c = deque()
stack_n = deque()
dic_c = {'+': 0, '-': 0, '*': 1, '/': 1}

for c in calc:
    if c.isalpha():
        stack_n.append(nums[ord(c) - 65])
    else:
        n2 = stack_n.pop()
        n1 = stack_n.pop()
        if c == '+':
            stack_n.append(n1 + n2)
        elif c == '-':
            stack_n.append(n1 - n2)
        elif c == '*':
            stack_n.append(n1 * n2)
        else:
            stack_n.append(n1 / n2)

print(f'{stack_n[0]:.2f}')