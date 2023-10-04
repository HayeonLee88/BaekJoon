# 11286번: 절댓값 힙 (최소 힙)
'''
절댓값 힙: 절댓값이 가장 작은 값 순으로 정렬한다. 절대값이 같은 경우 가장 작은 수가 우선.
연산의 개수: N (1≤N≤100,000)
x가 0이라면 가장 작은 값 출력, 제거
x가 0이 아니라면 배열에 x 저장
(x, 0/1) x가 양수이면 1, 음수이면 0

problem? 입력에서 0이 주어진 회수만큼 답을 출력 만약 배열이 비어있다면 0 출력

How?
    h: 절대값을 저장하는 최소 힙 (x, 0/1)
        x: 입력된 수의 절댓값, 0/1: 양수이면 1, 음수이면 -1
    1. 음수는 [절대값, -1] 저장, 양수는 [숫자, 1] 저장
    2. 출력시 절대값 * 부호 계산

'''
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

h = []
for _ in range(int(input())): # 연산 횟수만큼 반복
    num = int(input())
    if num == 0:
        if not h:
            print(0)
        else:
            x, sign = heapq.heappop(h)
            print(x * sign)
    else:
        if num < 0:
            sign = -1
            num = - num
        else: sign = 1
        heapq.heappush(h, [num, sign])
