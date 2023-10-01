# 2841번: 외계인의 기타 연주 (Stack, 구현)
'''
같은 줄에 여러 프렛을 누르면 가장 높은 프렛의 음이 연주됨

손가락으로 프렛을 한 번 누르거나 떼는 것을 손가락을 한 번 움직였다, 이때 손가락을 가장 적게 움직이는 횟수

첫째 멜로디에 포함된 음의 수 N, 한 줄에 있는 프렛 수P(1 ≤ N ≤ 500,000, 2 ≤ P ≤ 300,000)
다음 N개의 줄 멜로디 한 음을 나타내는 두 정수 (s_num, p_num)
(1 ≤ s_num ≤ N, 1 ≤ p_num ≤ P)

solution: 멜로디를 스택에 담아 다음 음이 연주될 때 해당 줄의 가장 높은 플렛(맨 위)과 비교한다. 이때 연주될 음이 더 높으면 append, 낮으면 해당음이 연주 될 때까지 pop을 하고 append, 같은 자리이면 continue.
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, p = map(int, input().split())
dic = dict()

cnt = 0
for i in range(n):
    s_num, p_num = map(int, input().split())
    try:
        latest_p = dic[s_num][-1]
        if p_num > latest_p:  # 연주할 음의 프렛이 제일 높은 프렛보다 높다면 누르기
            dic[s_num].append(p_num)
            cnt += 1
        elif p_num < latest_p:  # 연주할 음의 프렛이 제일 높은 프렛보다 낮으면 손가락 떼기
            while True:
                cnt += 1
                dic[s_num].pop()
                if not dic[s_num]:  # 손가락을 뗀 후 그 줄에 눌린 프렛이 없다면
                    latest_p = 0
                    break
                latest_p = dic[s_num][-1]  # 현재 가장 높은 프렛
                if p_num >= latest_p:  # 현재 가장 높은 프렛과 연주할 프렛이 같다면
                    break
            if p_num > latest_p:  # 손가락을 뗀 후 연주할 음이 안 눌려 있다면 누르기
                dic[s_num].append(p_num)
                cnt += 1
        else:  # 연주할 음이 가장 높은 음과 같다면
            continue

    except KeyError:  # 연주할 줄에 눌린 프렛이 없다면
        dic[s_num] = deque()
        dic[s_num].append(p_num)  # 손가락 누르기
        cnt += 1

print(cnt)

