# 11726번: 2xn 타일링
n = int(input())
if n == 1:
    print(1)
else:
    tiles = [0] * (n + 1)
    # [(i-1)에 2*1을 하나 붙여 만드는 개수,(i-2)에 1*2를 두개 쌓아 만드는 개수]
    tiles[1] = [1, 0]
    tiles[2] = [1, 1]
    for i in range(3, n + 1):
        a, b = tiles[i - 1]
        c, d = tiles[i - 2]
        tiles[i] = [(a + b) * 1, (c + d) * 1]

    print((tiles[n][0] + tiles[n][1]) % 10007)
