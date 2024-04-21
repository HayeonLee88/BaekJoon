import sys

sys.setrecursionlimit(100000)

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [list(input()) for i in range(n)]

answer = []
def search(x, y, n):
    global graph
    global answer
    now = graph[x][y] 
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != now:
                n //= 2
                answer.append('(')
                search(x, y, n)
                search(x, y + n, n)
                search(x + n, y, n)
                search(x + n, y + n, n)
                answer.append(')')
                return False
    answer.append(now)
    return True

search(0, 0, n)
print(*answer, sep='')