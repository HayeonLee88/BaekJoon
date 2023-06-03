# 4948번: 베르트랑 공준

import sys
input = lambda :sys.stdin.readline().rstrip()
data = [True] * 246913 # 123456x2 + 1
for i in range(2, int(246913**0.5)):
    j = 2
    while i * j < len(data):
        data[i*j] = False
        j += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(data[n+1:2*n+1].count(True))
