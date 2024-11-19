import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

indegree = [0] * (n + 1) 
graph = [[] for _ in range(n + 1)]

for i in range(m):
    seq = list(map(int, input().split()))
    for j in range(1, seq[0]):
        graph[seq[j]].append(seq[j + 1])
        indegree[seq[j + 1]] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for x in graph[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)
                
    if len(result) != n:
        print(0)
    else:
        for x in result:
            print(x)

topology_sort()