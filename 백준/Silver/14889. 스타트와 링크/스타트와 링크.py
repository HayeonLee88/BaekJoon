import sys
INF = 1e9

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = n // 2
array = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n 

def calc_stat(x):
    a = x
    b = list(range(n))

    for i in a:
        b.remove(i)
    ab = list(zip(a, b))

    a_hap= 0
    b_hap = 0
    for a_i, b_i  in ab:
        for a_j, b_j in ab:
            a_hap += array[a_i][a_j]
            b_hap += array[b_i][b_j]

    return abs(a_hap - b_hap)

answer = INF 
def backtracking(idx, cnt, state):
    global answer
    if cnt == m:
        tmp = calc_stat(state)
        if tmp == 0:
            print(0)
            exit()
        answer = min(answer, tmp)
        return
    
    else:
        for i in range(idx, n):
            if not visited[i]:
                state.append(i)
                visited[i] = True
                backtracking(i, cnt + 1, state)
                state.pop()
                visited[i] = False

backtracking(0, 0, [])
print(answer)