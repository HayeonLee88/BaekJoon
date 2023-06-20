# 2110번: 공유기 설치
'''
수직선 위에 집 N개, 각 집의 좌표는 x1, x2, ... , xN (단, 좌표는 모두 다르다.)
공유기 C개 설치
한 집에 공유기 하나만 설치 가능.
가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하는 방법은?
N: 2이상 200,000이하
C: 2이상 N이하
xi: 0이상 1,000,000,000이하

1 2 4 8 9: (1, 4, 8) or (1, 4, 9) 설치
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

n, c = map(int, input().split())
graph = [int(input()) for _ in range(n)]
graph.sort()

start = 1 # 최소 거리
end = graph[-1] - graph[0] # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이의 거리
    value = graph[0] # 첫번째 공유기 설치
    cnt = 1
    for i in range(1, n):
        # 탐색한 좌표가 (cnt)번째 공유기로부터 떨어진 거리가 mid 이상이라면
        if graph[i] >= value + mid:
            value = graph[i] # 새로운 공유기 위치
            cnt += 1
    if cnt >= c: # C개 이상으로 공유기를 설치할 수 있다면
        start = mid + 1 # 가장 인접한 공유기 사이의 거리 늘리기
        result = mid
    else: # C개 이상으로 공유기를 설치할 수 없다면
        end = mid - 1 # 가장 인접한 공유기 사이의 거리 줄이기

print(result)


