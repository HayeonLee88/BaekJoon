# 2887번: 행성 터널
'''
행성은 3차원 좌표의 한 점
두 행성을 연결할 때 드는 비용: 좌표의 두 행성의 각 x, y, z 차이 값 중 최솟값
총 터널 N-1개를 건설하여 모든 행성이 서로 연결되게 한다. 이때 필요한 최소 비용은?

입력
첫째 줄 행성의 개수: 1 ≤ N ≤ 100,000
다음 N개의 줄 각 행성의 x, y, z 좌표

solution
x, y, z를 기준으로 오름차순 정렬
옆에 있는 행성과의 거리를 기준으로 연결 비용 정하기
'''
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
planets_info = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets_info.append([i, x, y, z])

distances = []  # a, b, c: a와 b 행성 사이의 거리 c
planets_info.sort(key=lambda x: x[1])  # x좌표 기준으로 정렬
for i in range(n - 1):
    # i번째 행성 번호, i + 1번째 행성 번호, i번째 행성과 i + 1번째 행성 사이의 거리
    distances.append([planets_info[i][0], planets_info[i + 1][0], planets_info[i + 1][1] - planets_info[i][1]])

planets_info.sort(key=lambda x: x[2])  # y좌표 기준으로 정렬
for i in range(n - 1):
    # i번째 행성 번호, i + 1번째 행성 번호, i번째 행성과 i + 1번째 행성 사이의 거리
    distances.append([planets_info[i][0], planets_info[i + 1][0], planets_info[i + 1][2] - planets_info[i][2]])

planets_info.sort(key=lambda x: x[3])  # z좌표 기준으로 정렬
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
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않았다면 합치기
        union_parent(parent, a, b)
        cnt += 1
        answer += cost
    if cnt == n - 1: # 터널의 수가 n - 1개이면 멈추기
        break

print(answer)