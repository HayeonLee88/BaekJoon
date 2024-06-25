import sys

sys.setrecursionlimit(100000)
n = int(input())

eggs = [list(map(int, input().split())) for _ in range(n)]

answer = [0]
def backtracking(idx, cnt):
    if cnt == n:
        print(n)
        exit()

    if idx == n:
        answer.append(cnt)
        return
    
    if eggs[idx][0] <= 0:
        backtracking(idx + 1, cnt)
    
    else:
        for i in range(n):
            tmp = cnt
            if i == idx:
                continue
            if eggs[i][0] > 0:
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                if eggs[idx][0] <= 0:
                    tmp += 1
                if eggs[i][0] <= 0:
                    tmp += 1
                backtracking(idx + 1, tmp)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
            else:
                backtracking(idx + 1, tmp)

backtracking(0, 0)
print(max(answer))
