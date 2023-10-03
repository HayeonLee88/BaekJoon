# 4889번: 안정적인 문자열 (Stack)
'''
여는 괄호와 닫는 괄호만으로 이루어진 문자열이 주어진다.
문자열의 길이가 2000을 넘는 경우는 없고, 항상 길이는 짝수이다.
입력의 마지막 줄은 '-'가 한 개 이상 주어진다.

problem? 테스트 케이스 번호와 안정적인 문자열을 만들기 위한 최소 연산의 수를 출력

(cf. 괄호 2개씩 쌍을 지어 탐색하기 X)

stack: 열린 괄호를 담는 stack
cnt: 문자열 탐색 중 문자가 짝이 맞지 않는 '}'이 나오면 '{'로 바꾸는 횟수를 저장하는 변수
answer: stack 길이 // 2 + cnt

How?
     1. 문자열 탐색 중 문자가 '{' 이면 stack에  '{' 추가
     2. 문자열 탐색 중 문자가  '}'일 때 stack이 비어 있지 않다면 짝이 되는 가장 위의 '{' pop
     3. stack이 비었다면 짝이 없는 '}'를 '{'로 바꾼 후 stack에 담고, cnt += 1
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

i = 1 # 테스트 케이스 횟수
while True:
    s = input()
    if s[0] == '-':
        break
    stack = [] # '{'을 담을 스택
    cnt = 0
    for x in s:
        if x == '{': # 열림 괄호 스택에 넣기
            stack.append(x)
        else:
            if stack: # 짝이 맞는 괄호이므로 stack에서 '{' 제거
                stack.pop()
            else: # '{'이 올 차례에 '}'이 왔을 때 열림 괄호로 바꿔 스택에 추가
                stack.append('{')
                cnt += 1
    print(f'{i}. {len(stack) // 2 + cnt}')
    i += 1