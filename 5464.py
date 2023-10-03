# 5464번: 주차장 (최소 힙, 큐)
'''
1부터 N까지 번호가 매겨진 N개의 주차 공간

1. 차 도착 -> 비어있는 주차 공간이 있는지를 검사
2. 비어있는 공간이 없으면, 차량을 빈 공간이 생길 때까지 입구에서 기다리기
3. 빈 주차 공간이 하나만 있거나 차 한 대가 나가면 곧바로 그 장소에 주차를 하기
4. 빈 주차 공간이 여러 곳이면 번호가 가장 작은 주차 공간에 주차
5. 여러 대의 차량이 도착하면, 일단 도착한 순서대로 입구의 대기장소에서 줄서기

-대기장소는 큐(queue) FIFO, deque
-주차장은 우선순위 큐 heapq
-차량 요금: 차량의 무게 * 공간 요금

problem? M대의 차량이 주차장을 이용한다. 이때 수입은
'''
import sys
import heapq
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


wait_list = deque()
parking_lot = []
answer = 0
n, m = map(int, input().split())

for i in range(1, n + 1):
    heapq.heappush(parking_lot, i) # 공간 번호

costs = [int(input()) for _ in range(n)] # 각 공간의 단위 무게당 금액
weights = [] # 차의 무게를 담는 리스트
for i in range(1, m + 1):
    weights.append(int(input())) # 무게

parked = dict(zip(range(1, m + 1), [0] * n)) # {car_num(keys): parking_num(values)} 딕셔너리 초기화

for i in range(2 * m):
    car = int(input())
    if car > 0:
        if parking_lot:
            num = heapq.heappop(parking_lot) # 제일 작은 번호 공간 pop
            answer += weights[car - 1] * costs[num - 1] # 비용 더하기
            parked[car] = num # 차가 주차된 공간 저장
        else: # 입구에 대기
            wait_list.append(car)
    else:
        if wait_list: # 대기 중인 차가 있다면 새로운 차 바로 들어오기
            nxt_car = wait_list.popleft() # 입구 제일 앞 차 popleft
            num = parked[-car] # 차가 나온 주차 공간 번호
            parked[-car] = 0
            parked[nxt_car] = num # 새로 들어온 차가 주차된 공간 저장
            answer += weights[nxt_car - 1] * costs[num - 1] # 비용 더하기
        else: # 대기 중인 차가 없다면
            num = parked[-car] # 차가 나온 주차 공간 번호
            parked[-car] = 0
            heapq.heappush(parking_lot, num) # 빈 주차 장소 생김

print(answer)