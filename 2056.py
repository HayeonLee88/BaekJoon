# 2056번: 작업(DFS, Graph)
'''
수행해야 할 작업 N개 (3 ≤ N ≤ 10000),각각의 작업마다 걸리는 시간(1 ≤ 시간 ≤ 100)이 정수로 주어진다.
몇몇 작업들 사이에는 선행 관계라는 게 있어서, 어떤 작업을 수행하기 위해 반드시 먼저 완료되어야 할 작업들이 있다.

problem: 모든 작업을 완료하기 위해 필요한 최소 시간을 구하여라.
         물론, 서로 선행 관계가 없는 작업들은 동시에 수행 가능하다.

How?
    infos: 각 작업의 정보를 담는 리스트
    graph: 각 작업의 선행 작업을 담는 리스트
    visited: 작업이 끝났는지 확인하는 리스트
    timetable: 각 작업의 종료 시간을 담는 리스트
'''
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)] # 각 작업의 정보를 초기화 한다.
graph = [[] for _ in range(n)]
visited = [False] * n

timetable = [0] * n

i = 0
for info in infos: # 각 작업의 선행 작업을 초기화한다.
    if info[1]:
        for pre in info[2:]:
            graph[i].append(pre)
    i += 1


def dfs(start, time): # 작업 번호, 선행 작업 종료 시간
    if graph[start]: # 선행 작업이 있다면
        for pre in graph[start]:
            pre -= 1
            if visited[pre]: # 선행 작업이 끝났다면, 선행 작업의 종료 시간을 비교하여 time에 저장한다
                time = max(time, timetable[pre])
            else: # 선행 작업이 끝나지 않았다면, 선행 작업을 실행한다.
                time = max(time, dfs(pre, time))
        return time + infos[start][0] # 선행 작업 시간과 현재 작업 시간을 더하여 return
    else: # 선행 작업이 없다면 현재 작업 시간 return
        return infos[start][0]


for i in range(n): # 각 작업을 실행한다.
    visited[i] = True # 작업이 실행됐다면 True
    timetable[i] = dfs(i, 0) # 작업 종료 시간을 타임테이블에 저장한다.

print(max(timetable)) # 가장 늦게 끝나는 작업의 시간을 출력
