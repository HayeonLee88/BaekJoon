# Q42. 탑승구
'''
1번부터 G번까지의 번호로 구분된 탑승구
P개긔 비행기가 차례때로 도착
i번째 비행기를 1번부터 gi번째 (1 ≤ gi ≤ G) 탑승구 중 하나에 영구적으로 도킹
    도킹을 할때 다른 비행기가 도킹하지 않은 탑승구에만 가능하다.
    만약 어떤 탑승구에도 도킹할 수 없을 때 공항의 운행 중지
1 ≤ G ≤ 100,000 / 1 ≤ P ≤ 100,000
비행기를 최대 몇 대 도킹할 수 있는지 출력하라
첫째 줄 G
둘째 줄 P
다음 P개의 줄: 탑승구 정보 gi (i번째 비행기가 1번째부터 1 ≤ gi ≤ G인 gi번째 탑승구 중 하나에 도킹이 가능함을 의미)

가능한 가장 큰 번호의 탑승구부터 도킹 > 앞의 탑승구와 union (루트를 현재 번호-1로 만들기)
'''
import sys

input = lambda: sys.stdin.readline().rstrip()


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


gates = int(input())
planes = int(input())
parent = [0] * (gates + 1)
for i in range(1, gates + 1):
    parent[i] = i  # 부모를 자기 자신으로 초기화

answer = 0
for _ in range(planes):
    data = find_parent(parent, int(input()))  # 현재 비행기의 탑승구의 루트 확인
    if data == 0:  # 도킹 가능한 탑승구가 없을 경우
        break
    union_parent(parent, data, data - 1)  # 도킹이 가능할 경우 바로 앞의 탑습구와 합치기
    answer += 1

print(answer)
