# 4889번: 안정적인 문자열 (Stack)
'''
여는 괄호와 닫는 괄호만으로 이루어진 문자열이 주어진다.
여기서 안정적인 문자열을 만들기 위한 최소 연산의 수를 구하려고 한다.
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

t = 1
while True:
    q = deque()  # '{'을 담을 스택
    brakets = input()
    if brakets[0] == '-':
        break
    cnt = 0
    for braket in brakets:
        if braket == '{': # 열림 괄호 스택에 넣기
            q.append(braket)
        else:
            if not q: # '{'이 올 차례에 '}'이 왔을 때 열림 괄호로 바꿔 스택에 추가
                q.append('{')
                cnt += 1
            else: # 짝이 맞는 괄호이므로 stack에서 '{' 제거
                q.pop()
    cnt += len(q) // 2 # 짝이 맞지 않은 열림 괄호의 수를 2로 나눠 필요한 닫힘괄호'}' 수를 구함

    print(f'{t}. {cnt}')
    t += 1
