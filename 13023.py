# 13023번: ABCDE(DFS, BackTracking)
'''
N: 사람의 수 (5 ≤ N ≤ 2000)
M: 친구 관계의 수 (1 ≤ M ≤ 2000)
M개의 줄에는 정수 a와 b: a와 b가 친구라는 뜻

problem: 다음과 같은 친구 관계가 존재하면 1, 아니라면 0
    - A는 B와 친구다.
    - B는 C와 친구다.
    - C는 D와 친구다.
    - D는 E와 친구다.

How?
    a b 가 주어졌을 때 a b는 양방향 그래프이다.
    친구관계를 그래프로 나타내고, 깊이 우선 탐색으로 해당 친구관계부터 이어지는 친구관계가 4개가 있는지 확인한다.
    1/0으로 체크하는 것보다 True/False으로 체크하는게 더 빠르다
'''
# 6:34~52
import sys
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n)] # 0 ~ n - 1번 사람의 친구 관계를 담을 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 양방향 그래프이므로 친구 관계를 a와 b 모두에 저장한다.
    graph[b].append(a)

def DFS(x, cnt):
    global answer
    visited[x] = True # x번째 사람 방문 True
    if cnt == 4: # 이어진 관계가 4개라면 answer = 1
        answer = 1
        return
    else:
        for i in graph[x]:
            if not visited[i]:
                DFS(i, cnt + 1)
    visited[x] = False # x번째 사람 방문 Fasle로 초기화

answer = 0 # 조건에 맞는 친구관계를 나타내는 변수 초기화
visited = [False] * (n + 1) # n명의 사람들의 친구관계 탐색 유무를 저장하는 리스트 초기화

for i in range(n):
    DFS(i, 0) # 0번째 사람과 이어진 친구관계 0번에서 시작
    if answer: # 이어지는 네개의 관계가 존재하면 break
        break

print(answer)