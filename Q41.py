# Q41. 여행 계획
'''
1~N번의 여행지
여행 계획에 속한 도시의 수 M
1 ≤ N, M ≤ 500
N x N 행렬 = 두 여행지가 연결되어 있는지 여부 (1이면 연결)
마지막 줄 여행계획에 포함된 여행지의 번호

방법 1. BFS를 통해 여행 계획 내의 여행지 간의 연결을 확인하기
방법 2. union 연산을 통해 집합을 만들어 여행 계획에 해당하는 모든 여행지가 같은 집합에 속하는지 확인하기

방법 1과 방법 2의 효율성 차이가 크지 않다.
'''

import math
import time
import sys
from collections import deque


# 방법 1. BFS를 통해 여행 계획 내의 여행지 간의 연결을 확인하기

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

start = time.time()
math.factorial(100000)
graph = [[] for _ in range(n + 1)] # 연결된 노드를 담는 리스트 초기화
for i in range(n):
    for j in range(n):
        if data[i][j]: # 연결된 경우 해당 노드 추가
            graph[i + 1].append(j + 1)

def BFS(start, end): # 넓이 우선 탐색으로 현재 여행지와 다음 여행지의 연결을 확인한다.
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        visited[now] = True
        for node in graph[now]:
            if not visited[node]: # 현재 여행지에서 탐색하지 않은 여행지라면
                if node == end: # 탐색한 여행지가 끝 여행지라면 True 리턴
                    return True
                q.append(node)
    return False # 현재 여행지와 다음 여행지가 연결되지 않았다면

answer = 'YES'
if m != 1: # 여행 계획에 속한 여행지의 개수가 2개 이상일 때
    for i in range(m - 1):
        visited = [False] * (n + 1)
        if BFS(plan[i], plan[i + 1]): # 여행 계획의 현재 여행지와 다음 여행지가 연결되었다면
            continue
        else: # 여행 계획의 현재 여행지와 다음 여행지가 연결도지 않았다면
            answer = 'NO'
            break
print(answer)
end = time.time()
print(f"{end - start} sec")


# 방법 2. union 연산을 통해 집합을 만들어 여행 계획에 해당하는 모든 여행지가 같은 집합에 속하는지 확인하기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 총 여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화
start = time.time()
math.factorial(100000)


# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# union 연산 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 union연산 수행
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

answer = 'YES'
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        answer = 'NO'
print(answer)
end = time.time()
print(f"{end - start} sec")


'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3


5 5
0 1 0 0 0
1 0 1 0 0
0 1 0 1 0
0 0 1 0 0
0 0 0 0 0
1 2 3 4 5

'''