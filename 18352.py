# 18352번: 특정 거리의 도시 찾기
'''
노드: N개
단방향 간선: M개
거리: 1
도시 X에서 출발~ 도착한 모든 도시 중 최단 거리가 K인 모든 도시의 번호 출력
X~X: 거리 = 0
(2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
'''
import sys
from collections import deque
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

answer = []
def bfs(start):
    q = deque([start])
    dist = 0
    distance[start] = dist
    while q:
        now = q.popleft()
        dist = distance[now] + 1 # 현재 위치의 최단거리 + 1
        for city in graph[now]:
            if distance[city] == INF : #처음 방문한 경우
                distance[city] = dist
                q.append(city)
                if dist == k:
                    answer.append(city)

bfs(x)
answer.sort()
if len(answer) < 1:
    print(-1)
else:
    for a in answer:
        print(a)