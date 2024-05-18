import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
chickens = [] 
houses = [] 

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        x = row[j]
        if x == 1:
            houses.append([i, j])
        elif x == 2:
            chickens.append([i, j])

distances = []
for chicken in chickens:
    tmp = []
    for house in houses:
        tmp.append(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
    distances.append(tmp)

com_chicken = list(combinations(range(len(chickens)), m))
answer = [] 
for com in com_chicken:
    chicken_len = []
    for i in range(len(houses)):
        min_dist = 100
        for j in com:
            min_dist = min(min_dist, distances[j][i])
        chicken_len.append(min_dist)  
    answer.append(sum(chicken_len))  

print(min(answer))