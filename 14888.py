# 14888번: 연산자 끼워넣기
'''
N개로 이뤄진 수열
수와 수 사이에 끼워 넣을 수 있는 연산자 N-1개 (+, -, x, /)
주어진 수열의 순서 그대로 수 사이에 연산자를 넣어 수식을 만든다.\
N(2 ≤ N ≤ 11)
N-1인 4개의 정수 : +, -, x, /의 개수
problem: 수열과 연산자를 이용해 만들 수 있는 식의 결과 최댓값 출력 둘째줄 최솟값 출력
'''
from itertools import permutations

n = int(input())
sequence = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
operators = ['+'] * operator_cnt[0] + ['-'] * operator_cnt[1] + ['*'] * operator_cnt[2] + ['//'] * operator_cnt[3]
operator_seq = set(permutations(operators, n - 1))
answer = []

for ops in operator_seq:
    tmp = sequence[0]
    for i in range(n-1):
        op = ops[i]
        if op == '+':
            tmp += sequence[i+1]
        elif op == '-':
            tmp -= sequence[i + 1]
        elif op == '*':
            tmp *= sequence[i + 1]
        else:
            if tmp < 0 :
                tmp = - (- tmp // sequence[i + 1])
            else:
                tmp //= sequence[i + 1]
    answer.append(tmp)

print(max(answer))
print(min(answer))



