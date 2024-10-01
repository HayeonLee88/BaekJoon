import sys

input = lambda:sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parent = [i for i in range(n)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])  # 경로 압축
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    elif b > a:
        parent[b] = a


for i in range(n):
    for j in range(n):
        if graph[i][j]:
            union_parent(i, j)

answer = 'YES'
prev = parent[plan[0] - 1]
for i in range(1, m):
    now = parent[plan[i] - 1]
    if now != prev:
        answer = 'NO'
        break

print(answer)