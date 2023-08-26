# Q40: 숨바꼭질 (다익스트라)
'''
1~N번의 숨을 공간(헛간)
M개의 양뱡향 통로
최단거리 = 지나야 하는 길의 최소 개수
2 ≤ N ≤ 20,000
1 ≤ M ≤ 50,000
1번 헛간에서 최단 거리가 가장 먼 헛간을 구하라 (최단 거리가 같다면 가장 작은 헛간 번호 출력)
출력:
    숨어야 할 헛간 번호, 헛간까지의 거리, 같은 거리를 갖는 헛간의 개수
'''
import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance[1] = 0  # 시작 위치

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:  # 이미 탐색한 헛간이라면
            continue
        for node in graph[now]:  # 현재 헛간의 통로 탐색
            cost = dist + 1
            if cost < distance[node]:  # 현재 헛간을 거쳐가는 거리가 더 짧을
                distance[node] = cost
                heapq.heappush(q, (node, cost))

dijkstra(1)

max_node, max_distance = 0, 0
answer = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        answer = [max_node]
    elif max_distance == distance[i]: # 최단 거리가 같은 노드가 존재할 때
        answer.append(i)

print(max_node, max_distance, len(answer))

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''