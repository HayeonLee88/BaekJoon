# 2309번: 일곱난쟁이
from itertools import combinations
data = [int(input()) for _ in range(9)]
data.sort()
seven_dwarfs = list(combinations(data, 7))
print(seven_dwarfs)

for seven in seven_dwarfs:
  if sum(seven) == 100:
    for dwarf in seven:
      print(dwarf)
    break