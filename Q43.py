# Q43. 어두운 길
'''
N개의 집과 M개의 도로
각 집은 0 ~ N - 1번으로 구분
모든 도로에 가로등이 존재. 이 가로등을 하루동안 켜기 위한 비용은 해당 도로의 길이와 동일
일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하시오.
1 ≤ N ≤ 200,000 / N - 1 ≤ M ≤ 200,000
첫째 줄: N M
다음 M개의 줄: X Y Z ( 0 ≤ X, Y < N)  X<->Y 사이에 길이가 Z인 양방향 도로 존재
크루스칼: 1. 비용을 기준으로 오름차순 정렬을 한다.
        2. 비용이 적은 도로 순으로 연결할 때 집과 집 사이에 사이클이 생기는지 확인한다.
        3-1. 사이클이 생기지 않는다면 도로를 연결한다.
        3-2. 사이클이 생긴다면 해당 도로의 비용을 절약 금액에 합한다.
'''
import sys

input = lambda: sys.stdin.readline().rstrip()


def find_parent(parent, x): # 집의 루트를 찾는다.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b): # 도로 가로등을 켜 각 집의 집합을 합친다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * n  # 부모 테이블 초가화
graph = [list(map(int, input().split())) for _ in range(m)]  # 도로의 정보를 담는 리스트
graph.sort(key=lambda x: x[2])  # 비용을 기준으로 도로 오름차순 정렬

for i in range(n):
    parent[i] = i  # 부모 테이블을 자기 자신으로 초기화

save_money = 0 # 절약한 비용 초기화
for x, y, z in graph:
    if find_parent(parent, x) != find_parent(parent, y): # 사이클이 발생하지 않는다면 도로 가로등 켜기
        union_parent(parent, x, y)
    else:  # 사이클이 발행하는 경우 절약 금액에 비용 더하기
        save_money += z

print(save_money)

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
