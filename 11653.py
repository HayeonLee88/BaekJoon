# 11653번: 소인수분해
# 1 <= N <= 10,000,000
n = int(input())
answer = set()
for i in range(2, n // 2 + 1):
    while True:
        if n % i == 0:
            n //= i
            print(i)
        else:
            break
    if n == 1:
        break
if n != 1:
    print(n)
