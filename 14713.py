# 14713번: 앵무새 (큐)
'''
앵무새의 수: N (1 ≤ N ≤ 100)
N개의 줄에 걸쳐 각 앵무새가 말한 문장: Si (1 ≤ i ≤ N, 1 ≤ Si를 이루는 단어 수 ≤ 100, 1 ≤ 단어의 영소문자 수 ≤ 100)
cseteram이 받아 적은 문장: L (1 ≤ L을 이루는 단어 수 ≤ 10000, 각 단어는 1개 이상 32개 이하의 영문 소문자)

problem: 문장 L이 가능한 문장이라면 Possible을, 불가능한 문장이라면 Impossible을 출력한다.

How?
    각 앵무새가 말한 문장을 queue에 담아 큐의 첫 단어를 비교하여 일치하면 pop한다.
    앵무새가 말한 문장으로 문장 L을 만든 후 앵무새가 말한 단어가 남아있을 수 있다.
    따라서 문장 L의 단어의 개수와 모든 앵무새가 말한 문장 속 단어 개수의 합이 일치해야 한다.
'''
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
strings = [] # 각 앵무새가 말한 문장들 큐를 담을 리스트
s_words = 0
for _ in range(n):
    q = deque(input().split())
    strings.append(q)
    s_words += len(q)

answer = 'Possible'
L = input().split()

if len(L) != s_words:
    answer = 'Impossible'
else:
    for word in L: # 문장 L의 처음부터 일치하는 단어가 있는지 탐색
        print(f'L의 문장 중 단어: {word}')
        check = False
        for i in range(n):
            if strings[i] and strings[i][0] == word:
                print(f'{i}번째 앵무새가 말한 문장 속 단어: {strings[i][0]}')
                strings[i].popleft()
                check = True
                break

        if not check:
            answer = 'Impossible'
            break

print(answer)