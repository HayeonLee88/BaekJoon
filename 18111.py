# 18111번: 마인크래프트
'''
1. (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣기 -> 2초
2. 인벤토리에서 블록을 꺼내 (i, j) 가장 위에 놓기 -> 1초
땅 크기: N x M
B: 인벤토리에 있는 블록의 수
(1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7, 땅의 높이는 256을 초과할 수 없다)

땅 고르기 작업의 최소 시간과 그 경우 땅의 높이를 출력하라
답이 여러 개 라면 그 중 땅의 높이가 가장 높은 것을 출력하라

인벤토리의 블록 수가 0이라면 1번 작업만 할 수 있다.
'''
import sys

INF = int(1e9)
input = lambda: sys.stdin.readline().rstrip()

n, m, b = map(int, input().split())
graph = []
for _ in range(n):
    graph += list(map(int, input().split()))

graph.sort(reverse=True) # 땅의 높이가 높은 순으로 정렬
min_h, max_h = graph[-1], graph[0]
time, height = INF, 0

def BruteForce(h):
    blocks = b
    t = 0
    for i in range(n * m): # 제일 높은 땅부터 차례대로 땅 고르기
        '''
        제일 높은 땅부터 시작하면 인벤토리에 블록이 가장 많이 쌓이고 반복을 최소화할 수 있다.
        또한 블록이 충분하지 않은 순간이 온다면 땅 고르기를 멈춘다.
        '''
        now = graph[i]
        if now > h: # 현재 땅이 고르려는 땅의 높이보다 높을 때
            t += 2 * (now - h) # (초과하는 땅의 높이 * 2)만큼 시간 추가
            blocks += (now - h) # 인벤토리 블록 추가
        elif now < h: # 현재 땅이 고르려는 땅의 높이보다 낮을 때
            if blocks < h - now: # 올릴 수 있는 블록의 수가 모자르다면 멈추기
                t = INF
                break
            else: # 블록 쌓기
                t += (h - now) # 쌓는 블록의 수만큼 시간 추가
                blocks -= (h - now) # 인벤토리 블록 빼기
    return t # 시간 리턴

# 가장 낮은 땅부터 가장 높은 땅의 높이까지 BruteForce
for i in range(min_h, max_h + 1):
    tmp = BruteForce(i)
    if time >= tmp: # 시간이 같을 때 가장 높은 것을 출력하기 위해 걸리는 시간이 작거나 같을 떄 확인
        time = tmp
        height = i

print(time, height)