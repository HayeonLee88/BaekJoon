import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
cnt = 0

graph = defaultdict(lambda : {'parent':'', 'child':[], 'c':0})
for i in range(n + m):
    parent, f, c = input().split()
    c = int(c)
    graph[f]['parent'] = parent
    graph[f]['c'] = c
    graph[parent]['child'].append(f)


def search(now, types):
    global cnt

    for nxt in graph[now]['child']:
        if graph[nxt]['c']:
            search(nxt, types)
        else:
            cnt += 1
            types.add(nxt)
    return cnt

q = int(input())
for i in range(q):
    folder = input().split('/')[-1]
    types = set()
    cnt = 0
    answer = search(folder, types)
    print(len(types), answer)
