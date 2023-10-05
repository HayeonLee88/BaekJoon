# 15903번: 카드 합체 놀이(우선순위 큐)
'''
1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

n: 카드의 개수를 나타내는 수 (2 ≤ n ≤ 1,000)
m: 카드 합체를 몇 번 하는지를 나타내는 수 (0 ≤ m ≤ 15×n)

problem? n개의 카드로 m번의 카드 합체를 했을 때 만들 수 있는 가장 작은 점수를 출력

How?
    작은 순으로 정렬하여 가장 작은 숫자 카드 두장이 나오도록한다.
    최소 큐에 이 두 값을 더한 값을 두 번 저장한다.
'''
import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())

tmp = list(map(int, input().split()))
h = []
for i in tmp: # 카드 우선순위 정렬
    heapq.heappush(h, i)

for i in range(m):
    a1, a2 = heapq.heappop(h), heapq.heappop(h)
    new_a = a1 + a2
    heapq.heappush(h, new_a)
    heapq.heappush(h, new_a)

print(sum(h))
