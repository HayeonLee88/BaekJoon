# 15649번: N과 M
from itertools import permutations
n, m = map(int, input().split())
answer = list(permutations(range(1, n + 1), m))
for a in answer:
    for i in range(m):
        print(a[i], end=' ')
    print()