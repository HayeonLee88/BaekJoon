# 4375번: 1 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

import sys
input = lambda:sys.stdin.readline().rstrip()

while True:
    try:
        n = int(input())
    except:
        break
    num = 1
    answer = 1
    while True:
        if num % n == 0:
            print(answer)
            break
        num = num * 10 + 1
        answer += 1