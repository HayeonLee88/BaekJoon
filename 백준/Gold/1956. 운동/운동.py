import sys


INF = int(1e9)
input = lambda:sys.stdin.readline().rstrip()

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신은 비용 0으로 갱신
for i in range(1, v + 1):
    graph[i][i] = 0

# a -> b 비용 c로 갱신
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드-워셜 알고리즘에 따라 최단 거리 갱신
# a -> i -> b 
for i in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])


answer = INF
# a -> b -> ... -> a 최단 거리 찾기
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            continue
        answer = min(answer, graph[a][b] + graph[b][a])

print(answer if answer != INF else -1)