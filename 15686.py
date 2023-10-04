# 15686번: 치킨 배달(BruteForce, Combinations)
'''
N×N: 도시 크기
(r, c) 칸: 빈 칸(0), 치킨집(2), 집(1) (r과 c는 1부터 시작)
치킨 거리: 집과 가장 가까운 치킨집 사이의 거리 ((r1, c1)과 (r2, c2) => |r1-r2| + |c1-c2|)
도시의 치킨 거리: 모든 집의 치킨 거리의 합

집의 개수는 2N개를 넘지 않고, M은 1 ≤ M ≤ 13

problem? 치킨집을 최대 M개 골랐을때, 도시의 치킨 거리의 최솟값을 출력하라

how?    min_dist: 각 집의 치킨거리 100으로 초기화. 도시의 최대 크기 50*50 이므로 치킨 거리는 100이 될 수 없다.
        chicken_len: 각 집의 치킨 거리를 저장하는 리스트
        answer: 치킨집이 m개일 때 모든 조합의 도시의 치킨 저장하는 리스트
'''
import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
chickens = []  # 치킨집의 위치를 담는 리스트 초기화
houses = []  # 집들의 위치를 담는 리시트 초기화

for i in range(n):  # 도시를 돌며 치킨집과 집의 위치 저장
    row = list(map(int, input().split()))
    for j in range(n):
        x = row[j]
        if x == 1:
            houses.append([i, j])
        elif x == 2:
            chickens.append([i, j])

distances = []
for chicken in chickens: # 모든 치킨집과 모든 집 사이의 거리를 미리 구한다.
    tmp = []
    for house in houses:
        tmp.append(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
    distances.append(tmp)

# M개 중 어떤 치킨 집이 남을 지 정한다.
com_chicken = list(combinations(range(len(chickens)), m))
answer = []  # 조합별 도시의 치킨 거리를 담는 리스트
for com in com_chicken: # 남는 치킨집의 조합
    chicken_len = []
    for i in range(len(houses)):
        min_dist = 100 # 각 집마다 M개의 치킨거리 중 가장 짧은 거리를 담는다.
        for j in com:
            min_dist = min(min_dist, distances[j][i])
        chicken_len.append(min_dist)  # 최소 치킨 거리 저장
    answer.append(sum(chicken_len))  # 치킨 거리의 합 저장

print(min(answer))
