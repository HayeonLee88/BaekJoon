# 2493번: 탑(Stack)
'''
직선 위에 N개의 높이가 서로 다른 탑을 왼쪽부터 오른쪽 방향으로 차례로 세운다.
각 탑의 꼭대기에 레이저 송신기를 설치, 레이저는 수평 직선의 왼쪽 방향으로 발사
탑의 기둥에 레이저 신호를 수신하는 장치 존재하고, 레이저 신호는 먼저 만나는 하나의 탑에서만 수신한다.

probelm: 탑들의 개수 N과 탑들의 높이가 주어질 때,
각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는 지 알아내라
IF. 수신하는 탑이 존재하지 않으면 0을 출력

N (1 이상 500,000 이하)
N개의 탑들이 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 입력 (1 이상 100,000,000 이하의 정수)
'''

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
tops = list(map(int, input().split()))
former_tops = deque() # 위치마다 높은 탑을 저장하는 리스트

answer = []  # 정답을 담을 리스트
for i in range(n):
    now = tops[i]
    while former_tops:  # 이전 탑들과 비교
        if former_tops[-1][1] < now:  # 비교한 탑이 수신이 불가능할 때
            former_tops.pop()  # 작은 탑 제거
        else: # 비교한 탑이 수신 가능할 때
            answer.append(former_tops[-1][0] + 1)  # 수신할 탑의 위치 정답에 저장
            former_tops.append((i, now))  # 현재 탑 정보 저장
            break

    if not former_tops:  # 앞에 탑을 모두 탐색하고 수신할 수 있는 탑이 없다면
        answer.append(0) # 정답 0 저장
        former_tops.append((i, now)) # 현재 탑 정보 저장

print(*answer)