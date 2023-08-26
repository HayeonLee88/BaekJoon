# Q39. 화성탐사 (다익스트라)
'''
NxN 공간에 존재하는 화성 탐사 기계.
각 칸을 지나기 위한 비용(에너지 소비량)
[0][0]에서 [N-1][N-1]로 이동하는 최소 비용을 출력
화성 탐사 기계는 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.
T: 테스트 케이스 (10이하 자연수)
N: 탐사 공간 (2이상 125이하)
각 칸의 비용: 0이상 9이하
'''
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    def dijkstra(x, y):
        q = []
        heapq.heappush(q, [data[x][y], x, y]) # 현재 칸의 비용과 현재의 위치 x, y를 담는다.
        distance[x][y] = data[x][y]
        while q:
            dist, a, b = heapq.heappop(q)
            if distance[a][b] < dist: # 이미 탐색한 칸이라면
                continue
            for i in range(4): # 상 하 좌 우 이동
                nx = a + dx[i]
                ny = b + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: # 탐사 로봇이 공간을 벗어난다면
                    continue
                cost = data[nx][ny] + dist # 현재 위치의 비용 + 이전 이동 비용
                if cost < distance[nx][ny]: # 현재 위치를 거쳐 이동하는 비용이 더 작다면
                    distance[nx][ny] = cost
                    heapq.heappush(q, [cost, nx, ny])
    dijkstra(0, 0) # [0][0]부터 탐색
    print(distance[-1][-1])

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''