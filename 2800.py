# 2800번: 괄호 제거 (문자열, Stack)
from collections import deque
from itertools import product

calc = list(input())
answer = set()

open_brakets = deque() # 열린 괄호의 위치 담는 덱
all_brakets = deque() # 닫힌 괄호의 위치를 담는 덱
for i, c in enumerate(calc):
    if c == '(':
        open_brakets.append(i)
    elif c == ')': # 닫힘 괄호가 나왔다면 제일 마지막 열림 괄호의 위치와 함께 all_brakets에 저장
        all_brakets.append((open_brakets.pop(), i))

iter = [True, False]
cases = list(product(iter, repeat = len(all_brakets))) # 중복 조합으로 case 나누기

for case in cases:
    new_calc = calc[:]
    for i in range(len(all_brakets)):
        if not case[i]:
            new_calc[all_brakets[i][0]] = ''
            new_calc[all_brakets[i][1]] = ''

    answer.add(''.join(c for c in new_calc))

for c in list(sorted(answer))[1:]:
    print(c)


# comninations을 이용한 방법
'''
수식에서 올바른 괄호 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력한다.
수식은 숫자, '+', '*', '-', '/', '(', ')'로만 이루어짐.
수식의 길이는 최대 200, 괄호 쌍은 1개 이상 이하 10개

stack: 열린 괄호 위치를 담을 스택
brakets_indexes: 괄호 쌍의 인덱스를 담을 리스트 (열림 index, 닫힘 index)

How?
수식을 탐색할 때 열린 괄호가 나오면 그 위치를 stack에 append
닫힌 괄호가 나오면 stack 제일 위에 있는 열린괄호를 pop하고 괄호 쌍의 위치를 brakets_indexes에 append
combinations을 이용해 지워낼 괄호 쌍을 1개 ~ 모든 괄호 개수 만큼 뽑는다.

import sys
from collections import deque
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

stack = deque()
brakets_indexes = []
s = list(input())
for i, x in enumerate(s):
    if x == '(':
        stack.append(i) # 열린 괄호 위치 append
    elif x == ')':
        open_i = stack.pop() # 닫힘 괄호와 쌍이 되는 열린 괄호 위치 pop
        brakets_indexes.append((open_i, i)) # 괄호 쌍의 위치 저장

true_brakets = []
brakets_len = len(brakets_indexes)
for i in range(1, brakets_len + 1): # 1개 ~ 모든 괄호쌍 개수 만큼 지울 괄호쌍의 조합을 뽑는다. 
    true_brakets.append(list(combinations(brakets_indexes, i)))

answer = set() # 정답을 담을 집합 초기화
for bs in true_brakets: # 지울 1개 ~ 모든 괄호쌍 개수 조합을 담는 리스트
    for b in bs: # 지울 i개의 괄호쌍 조합
        tmp = s[:]
        for i in range(len(b)): # 뽑힌 괄호를 지운다
            tmp[b[i][0]] = ''
            tmp[b[i][1]] = ''
        answer.add(''.join(t for t in tmp)) # 만들어진 수식을 저장

for i in sorted(answer): # 오름차순으로 수식 출력
    print(i)
'''
