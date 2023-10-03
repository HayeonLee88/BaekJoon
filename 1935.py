# 1935번: 후위 표기식2 (Stack)
'''
첫째줄 N: 피연산자의 개수(1 ≤ N ≤ 26)
둘째줄 후위 표기식: 길이 100이하
셋째줄 ~ N+2줄 피연산자에 대응 하는 값: 100보다 작거나 같은 자연수

problem? 후위 표기식을 앞에서부터 계산한 결과를 소숫점 둘때 자리까지 출력하가

How?
    stack: 숫자를 담는다.
    answer: 문자열 탐색 후 stack에 남은 수
    dic: {피연산자(keys): 숫자(values)}
     1. 문자열 탐색 중 문자가 피연산자라면 피연산자에 대응하는 값을 stack에 저장
     2. 문자열 탐색 중 문자가 수식이라면 stack에서 숫자 두 개 pop
     3. stack은 FILO이므로 처음 나온 값이 수식의 두번째 위치, 나중에 나온 값이 수식의 첫번째 위치
     4. 수식을 계산한 값을 다시 stack에 저장
     5. 문자열 탐색이 끝날 때까지 1~4 진행
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dic = dict(zip(list(map(chr, range(65, 65 + n + 1))), [0] * n)) #{피연산자(keys): 숫자(values)}
s = input()
for i in range(n): # 피연산자에 대응하는 값 초기화
    dic[chr(i + 65)] = int(input())

stack = []
for x in s:
    if x.isalpha(): # 피연산자라면 피연산자에 대응하는 값을 stack에 저장
        stack.append(dic[x])
    else: # 수식이라면 stack에서 숫자 두 개 pop
        # (FILO 구조 스택) 처음 나온 값이 수식의 두번째 위치, 나중에 나온 값이 수식의 첫번째 위치
        n2 = stack.pop()
        n1 = stack.pop()
        if x == '+':
            n3 = n1 + n2
        elif x == '-':
            n3 = n1 - n2
        elif x == '*':
            n3 = n1 * n2
        else:
            n3 = n1 / n2
        stack.append(n3) # 수식을 계산한 값을 다시 stack에 저장

print(f'{stack[0]:.2f}') # 소수점 둘째 자리까지 표현하기