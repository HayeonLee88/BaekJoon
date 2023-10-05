# 14235번: 크리스마스 선물(우선순위 힙)
'''
아이들과 거점지를 방문한 횟수 n이 주어진다.(1≤n≤5,000)

problem? 차례대로 방문한 아이들과 거점지의 정보들이 주어졌을 때,
         아이들이 준 선물들의 가치들을 출력하시오. 만약 아이들에게 줄 선물이 없다면 -1

How?
    우선순위 힙을 사용하여 입력된 a의 값에 '-'부호를 붙여 저장해
    큰 순서대로 출력이 되도록 한다.
'''
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

h = []
n = int(input())

for i in range(n):
    a_list = list(map(int, input().split()))
    if a_list[0] == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(-1)
    else:
        for a in a_list[1:]:
            heapq.heappush(h, -a)