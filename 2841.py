# 2841번: 외계인의 기타 연주 (Stack, 구현)
'''
연주하는 음의 수: N, 한 줄의 프렛 수: P (1 ≤ N ≤ 500,000, 2 ≤ P ≤ 300,000)
모든 줄의 모든 프렛 = 6 * 300,000 = 1,800,000 메모리 부족
1번부터 6번 줄을 담는 리스트, 각 줄은 stack
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, p_num = map(int, input().split())
strings = [deque() for _ in range (7)]

answer = 0
for _ in range(n):
    i, now = map(int, input().split())
    while strings[i]:
        if strings[i][-1] > now: # 손가락 떼기
            strings[i].pop()
            answer += 1
        else:
            break
    # 해당 줄에 눌린 프렛이 없거나 더 작은 프렛이 눌려 있다면
    if not strings[i] or strings[i][-1] < now:
        strings[i].append(now)
        answer += 1

print(answer)