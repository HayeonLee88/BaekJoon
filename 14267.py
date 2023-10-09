# 14267번: 회사 문화1 (DFS, 그래프)
'''
상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬
n: 회사의 직원 수
m: 최초의 칭찬의 횟수 (2 ≤ n, m ≤ 100,000)
직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다.

problem: 1번부터 n번의 직원까지 칭찬을 받은 정도를 출력하시오.

How?
    people: i번째 직원의 직속 상사를 나타내는 리스트
    graph: i번째 직원의 직속 후배를 담는 리스트

tip: 1. 직속 상사가 같은 직원이 여러 명일 수 있다.
     2. 칭찬 받은 당사자에게만 칭찬 수치를 더한 후 마지막 번호의 사람부터 깊이우선탐색하여 직속 후배들에게도 점수를 준다.
'''
import sys

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
people = list(map(int, input().split()))
people.insert(0, 0)  # 1 ~ n번이므로 맨 앞 0추가

graph = [[] for _ in range(n + 1)]
for i, p in enumerate(people):
    if p != -1:
        graph[p].append(i)  # 직속상사 -> 직속 부하 담기

answer = [0] * (1 + n)


def DFS(start, weight):  # 내리 칭찬 점수를 더하는 깊이우선 탐색
    for below in graph[start]:
        DFS(below, weight)
        answer[below] += weight


for _ in range(m):  # 칭찬을 받은 당사자에게만 먼저 칭찬 수치를 더한다.
    i, w = map(int, input().split())  # i: 칭찬받은 직원 번호, w: 칭찬 수치
    answer[i] += w

for i in range(n - 1, 0, -1):  # 직속후배가 있는 가장 끝번호의 직속후배부터 내리칭찬 점수를 더한다
    if answer[i]:
        DFS(i, answer[i])

for i in range(1, n + 1):  # 사장부터 정답 출력하기
    print(answer[i], end=' ')
