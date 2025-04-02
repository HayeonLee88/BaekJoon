import sys

sys.setrecursionlimit(100000)

input = lambda:sys.stdin.readline().rstrip()

n, r, q = map(int, input().split())

# 연결된 간선
graph = [[] for i in range(n + 1)]
# 서브트리 정점의 수
subtree = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(x, par):
    subtree[x] = 1
    for nxt in graph[x]:
        if nxt == par:
            continue
        subtree[x] += dfs(nxt, x)
    return subtree[x]

dfs(r, 0)

for _ in range(q):
    print(subtree[int(input())])
            