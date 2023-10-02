# 5464번: 주차장 (최소 힙, 큐)
'''
1부터 N까지 번호가 매겨진 N개의 주차 공간

1. 차 도착 -> 비어있는 주차 공간이 있는지를 검사
2. 비어있는 공간이 없으면, 차량을 빈 공간이 생길 때까지 입구에서 기다리기
3. 빈 주차 공간이 하나만 있거나 차 한 대가 나가면 곧바로 그 장소에 주차를 하게
4. 빈 주차 공간이 여러 곳이면 번호가 가장 작은 주차 공간에 주차
5. 여러 대의 차량이 도착하면, 일단 도착한 순서대로 입구의 대기장소에서 줄을 서

-대기장소는 큐(queue) FIFO, deque
-주차장은 우선순위 큐 heapq
-차량 요금: 차량의 무게 * 공간 요금

problem? M대의 차량이 주차장을 이용한다. 이때 수입은
'''
import sys
from collections import deque
import heapq

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

parking_lot = []
for i in range(n):
    heapq.heappush(parking_lot, i)

cost = [int(input()) for _ in range(n)]
weight = [int(input()) for _ in range(m)]

dic = dict(zip(range(1, m + 1), [0] * m))  # 차(key): 주차장 번호(value)
arrival = deque()

answer = 0
for i in range(2 * m):
    car = int(input())
    if car > 0:
        if parking_lot:
            parking_n = heapq.heappop(parking_lot)  #
            dic[car] = parking_n  # 주차 장소 저장
            answer += cost[parking_n] * weight[car - 1]
        else:
            arrival.append(car)  # 입구에 대기
    else:
        parking_n = dic[-car]
        dic[-car] = 0
        if arrival:  # 대기 중인 차가 있다면 새로운 차 바로 들어오기
            nxt_car = arrival.popleft()
            dic[nxt_car] = parking_n
            answer += cost[parking_n] * weight[nxt_car - 1]
            continue
        heapq.heappush(parking_lot, parking_n)  # 빈 주차 장소 생김
print(answer)
