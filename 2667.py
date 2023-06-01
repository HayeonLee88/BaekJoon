# 2667 단지 번호 붙이기

import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    global num
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        num += 1
        return num
    return False
num = 0
num_list = [] #각 단지 내 집의 수를 담는 리스트의 길이는 단지의 개수
for i in range(n):
    for j in range(n):
        num = dfs(i, j)
        if num:
            num_list.append(num)

num_list.sort()
print(len(num_list))
for numb in num_list:
    print(numb)

