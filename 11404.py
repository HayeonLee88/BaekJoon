# 11401번: 플로이드 (최단 경로 문제)
'''
n(2 ≤ n ≤ 100)개의 도시
한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스
각 버스는 한 번 사용할 때 필요한 비용이 있다.
모든 도시 쌍 (A, B)에 대해 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하라
A에서 B로 갈 수 없다면 0 출력
'''
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (1 + n) for _ in range(1 + n)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    # 같은 노선의 버스 중 최소 비용이 적은 것을 선택
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # j > k 최소 비용: j > i(1~n) + i(i~n) > k 비용 비교
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()