import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))

total_weight = 0
time_table = deque()  # 다리 위로 올라오는 순으로 (트럭, 현재 시간) 저장
answer = 0
for time in range(1, w * n + 2):
    if time_table and time_table[0][0] == time:
        now_t, truck = time_table.popleft()
        total_weight -= truck
        if not time_table and not trucks:
            print(time)
            break

    if trucks and total_weight + trucks[0] <= l:
        truck = trucks.popleft()
        total_weight += truck
        time_table.append((time + w, truck))