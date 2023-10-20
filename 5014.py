# 5014번: 스타트링크 (BFS)
'''
F: 가장 높은 층 (1 ≤ S, G ≤ F ≤ 1000000)
S: 현재 층
G: 스타트링크가 있는 층
(0 ≤ U, D ≤ 1000000)
U: 위로 U층 가는 버튼 (0 ≤ U ≤ 1000000)
D: 아래로 D층 가는 버튼 (0 ≤ D ≤ 1000000)

problem: 첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다.
         만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.

How? 넓이 우선 탐색을 통해 S층에서 G층까지 가기 위해 누르는 버튼의 최소 횟수를 저장한다.

Tips: S와 G가 같은 층일 경우, 0층이 없는 것을 고려
'''
from collections import deque

f, s, g, u, d = map(int, input().split())
graph = [False] * (f + 1) # 건물의 모든 층을 False로 초기화
buttons = [u, -d] # 올라가기, 내려가기 버튼 리스트 초기화

def bfs(s):
    check = False # G층을 도달을 체크하는 변수
    q = deque()
    q.append(s)
    graph[s] = 0 # 시작 층은 0회
    while q:
        now = q.popleft()
        cnt = graph[now]
        for b in buttons:
            next = now + b
            if next < 1 or next > f or graph[next]:
                continue
            # 다음 층이 건물을 벗어나지 않고, 처음 오는 곳이라면
            graph[next] = cnt + 1 # 다음 층의 버튼 횟수를 (현재 버튼 횟수) + 1로 저장
            q.append(next)
            if next == g: # 만약 다음 층이 G라면
                check = True
                break
        if check:
            break
    return graph[g] # G층의 버튼 횟수 리턴

if s == g: # 같은 층일 떄
    print(0)
else:
    answer = bfs(s)
    print(answer if answer else "use the stairs")
