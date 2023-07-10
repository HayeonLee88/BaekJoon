# Q38. 정확한 순위 (플로이드워셜)
'''
학생들의 수 N: 2이상 500이하
두 학생의 성적 비교 횟수 M: 2이상 10,000이하
성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력하라
500 * 500 * 500 = 125,000,000
플로이드워셜 알고리즘 사용
'''
import sys
INF = int(1e9)
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
data = [0] * (n + 1)  # 연결된 노드의 수

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

answer = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF: # i > j로 갈 수 있거나 j > i로 갈 수 있다면
            cnt += 1
    if cnt == n: # i번째에서 모든 번호로 갈 수 있다면 +1
        answer += 1
print(answer)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
