from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    truck_weights = deque(truck_weights)
    passing = deque()

    while True:
        time += 1
        if passing:
            if passing[0][1] + bridge_length == time:
                truck_weight, _ = passing.popleft()
                total_weight -= truck_weight
                
        # 다리 위의 무게가 제한을 넘지 않는다면
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck_weight = truck_weights.popleft()
                passing.append([truck_weight, time])
                total_weight += truck_weight

        if not passing:
            break
            
    return time