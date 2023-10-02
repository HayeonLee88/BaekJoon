# 13335번: 트럭 (Queue)
'''
n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)
n: 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10), ai는 i번째 트럭의 무게
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split())) # 다리로 오르는 트럭의 순서

total_weight = 0 # 다리 위 총 트럭의 무게
time_table = deque()  # 다리 위로 올라오는 순으로 (트럭, 현재 시간) 저장
for time in range(1, w * n + 2): # 최대 시간 =  다리 길이 * 트럭 수 + 1
    # 타임테이블이 비어 있지 않고, 큐의 제일 앞 트럭의 도착시간에 도달했다면
    if time_table and time_table[0][0] == time:
        now_t, truck = time_table.popleft() # 타임 테이블에서 트럭 빼기
        total_weight -= truck # 지나간 트럭 무게 빼기
        if not time_table and not trucks: # 트럭이 다리를 모두 지나갔다면
            print(time)
            break
    # 다리를 지날 트럭이 남아있고, 제일 앞 트럭의 무게를 더했을 때 최대 하중을 넘지 않는다면
    if trucks and total_weight + trucks[0] <= l:
        truck = trucks.popleft() # 트럭 다리 건너기
        total_weight += truck # 트럭 무게 더하기
        time_table.append((time + w, truck)) # 타임 테이블에 (도착 시간, 트럭 무게) 저장