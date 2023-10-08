# 10810번: 공 넣기
'''
n, m = map(int, input().split())
basket = [0] * (n + 1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j + 1):
        basket[l] = k

print(*basket[1:])
'''
# 5:17~
n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
print(basket)
for time in range(m):
    i, j = map(int, input().split())
    basket = basket[:i - 1] + basket[j - n - 1: i - n - 2:-1] + basket[j:]

print(*basket)