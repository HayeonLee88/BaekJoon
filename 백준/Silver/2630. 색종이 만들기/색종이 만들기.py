import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

answer = {0: 0, 1: 0}

def search(x, y, n):
    global graph
    global answer
    now = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != now:
                n //= 2
                search(x, y, n)
                search(x + n, y, n)
                search(x, y + n, n)
                search(x + n, y + n, n)
                return False
    answer[now] += 1
    return True

search(0, 0, n)
print(f'{answer[0]}\n{answer[1]}', end='')
