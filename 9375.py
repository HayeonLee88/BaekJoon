# 9375번: 패션왕 신해빈
# 0 <= n <= 30, n이 0일 때를 고려하자

from functools import reduce

times = int(input())

for i in range(times):
  n = int(input())
  if n == 0:
    print(0)
    continue
  closet = {}
  closet.update()
  for j in range(n):
    value, key = input().split()
    if key in closet.keys():
      closet[key] += 1
    else:
      closet[key] = 2
  print(reduce(lambda x, y: x*y, closet.values()) - 1)