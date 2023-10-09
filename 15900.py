# 15900번: 나무 탈출 (그래프, BFS)
'''
N개의 정점이 있는 트리 (1번부터 N번)
N: 트리의 정점 개수(2 ≤ N ≤ 500,000)
루트노드: 1번 정점
리프노드: 자식이 없는 노드

모든 리프 노드에 게임말이 하나씩 놓여있는 채로 시작하고, 한 사람의 차례일 때 게임의 말을 부모 노드로 옮긴다.
이때 말이 루트노드로 오면 게임말은 즉시 제거 된다. 성원이를 얕본 형석이는 성원이를 먼저 시작하게 한다.

problem: 성원이가 최선을 다했을 때 이 게임을 이길 수 있으면 Yes, 아니면 No를 출력한다.

How?
    graph: 노드 사이의 간선 정보를 담는 리스트
    depth: 각 노드의 깊이를 나타내는 리스트
    리프노드는 graph[x]의 길이가 1이다.
    리프노드의 모든 깊이의 합을 구하여 이 값이 짝수이면 이길 수 없고, 홀수이면 이길 수 있다.

tip: 메모리 & RecursionError -> BFS로 풀기
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n + 1)]
depth = [-1 for _ in range(n + 1)] # -1: 아직 방문하지 않은 노드의 깊이를 나타냄
depth[1] = 0 # 루트노드 깊이
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def check_depth(start): # 리프노드의 깊이를 탐색
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if depth[next] == -1: # 아직 방문하지 않은 노드라면
                depth[next] = depth[now] + 1
                q.append(next)


check_depth(1) # 1번(루트노드)부터 시작하여 자식노드 탐색
cnt = 0
for i in range(2, n + 1):
    if len(graph[i]) == 1:
        cnt += depth[i]
print(depth)
print('Yes' if cnt % 2 != 0 else 'No')


