# 1929번: 소수 구하기. M이상 N이하의 소수를 모두 출력
# python3보다 pypy3가 더 빠름
m, n = map(int, input().split())
data = [True] * (n + 1)
data[1] = False # 1은 소수가 아니다
for i in range(2, n + 1):
    j = 2
    while i * j < n + 1:
        if data[i*j]:
            data[i * j] = False
        j += 1
for i in range(m, n + 1):
    if data[i]:
        print(i)