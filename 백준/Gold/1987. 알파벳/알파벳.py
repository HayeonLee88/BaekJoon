import sys
sys.setrecursionlimit(100000)

input = lambda:sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = []

visited_a = dict()

for _ in range (r):
    row = list(input())
    graph.append(row)
    for x in row:
        visited_a[x] = False

len_a = len(visited_a)
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtracking(x, y, cnt):
    global answer
    if cnt == len_a:
        print(cnt)
        exit() # 처음에 얘를 그냥 return으로 했다가 틀렸습니다..
    else:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < r and 0 <= ny < c:
                tmp = cnt
                alpha = graph[nx][ny]
                if not visited_a[alpha]:
                    visited_a[alpha] = True
                    backtracking(nx, ny, tmp + 1)
                    visited_a[alpha] = False

    answer = max(answer, cnt)
    return 

visited_a[graph[0][0]] = True

backtracking(0, 0, 1)
print(answer)