import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
planets_info = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets_info.append([i, x, y, z])

distances = []  # a, b, c: a과 b 행성 사이의 거리 c
planets_info.sort(key=lambda x: x[1])  # x좌표 기준으로 정렬
for i in range(n - 1):
    # i번째 행성 번호, i + 1번째 행성 번호, i번째 행성과 i + 1번째 행성 사이의 거리
    distances.append([planets_info[i][0], planets_info[i + 1][0], planets_info[i + 1][1] - planets_info[i][1]])

planets_info.sort(key=lambda x: x[2])  # y좌표 기준으로 정렬
for i in range(n - 1):
    # i번째 행성 번호, i + 1번째 행성 번호, i번째 행성과 i + 1번째 행성 사이의 거리
    distances.append([planets_info[i][0], planets_info[i + 1][0], planets_info[i + 1][2] - planets_info[i][2]])

planets_info.sort(key=lambda x: x[3])  # x좌표 기준으로 정렬
for i in range(n - 1):
    # i번째 행성 번호, i + 1번째 행성 번호, i번째 행성과 i + 1번째 행성 사이의 거리
    distances.append([planets_info[i][0], planets_info[i + 1][0], planets_info[i + 1][3] - planets_info[i][3]])

distances.sort(key=lambda x: x[2]) # 비용을 기준으로 정렬

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * n  # 부모 테이블 초기화
for i in range(n):
    parent[i] = i  # 부모 테이블의 값을 자기 자신으로 초기화

cnt = 0
answer = 0
for a, b, cost in distances:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1
        answer += cost
    if cnt == n - 1:
        break

print(answer)