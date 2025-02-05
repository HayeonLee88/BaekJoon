'''
9:33~
모든 전선을 탐색
하나의 전선을 끊었을 때 [v1, v2]
|v1과 이어진 송전탑의 개수 - v2과 이어진 송전탑의 개수|
이차원 리스트로 트리 표현
'''
from collections import deque
def solution(n, wires):
    answer = n
    visited = []
    graph = [[] for _ in range(n + 1)]
    
    def bfs(x):
        cnt = 1
        q = deque()
        q.append(x)
        while q:
            now = q.popleft()
            for x in graph[now]:
                if not visited[x]:
                    q.append(x)
                    visited[x] = True
                    cnt += 1
        return cnt
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        visited = [False] * (n + 1)
        visited[v1], visited[v2] = True, True
        answer = min(answer, abs(bfs(v1) - bfs(v2)))
        
        
    return answer