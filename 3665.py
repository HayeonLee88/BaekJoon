# 3665번: 최종 순위
'''
1:36~
1번부터 N번까지의 팀
작년 순위와 작년에 비해 상대적으로 올해의 순위가 바뀐 팀의 목록만 발표
이 정보를 통해 올해 최종 순위를 만들기.
입력
    테스트 케이스
    n (2 ≤ n ≤ 500)
    ti (1 ≤ ti ≤ n) 작년의 i등을 한 팀의 번호
    상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
    두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n)

출력
    만약 일관성이 없는 잘못된 데이터라면 IMPOSSIBLE
    확실한 순위를 찾을 수 없다면 ?
    확실한 순위를 찾았다면 1등팀부터 순서대로 n개의 정수 한 줄 출력

위상 정렬 사용
작년 순위에서 상대적으로 등수가 바뀐 쌍들의 정보를 적용했을 때
진입 차수가 1이 넘는 팀이 존재한다면: impossible
집입 차수가 0인 탐이 2개 이상이라면: ?
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
T = int(input())
n = int(input())
last_info = list(map(int, input().split()))

rank = [0] * (n + 1)
last_indegree = [1] * (n + 1)
last_indegree[last_info[0]] = 0

last_graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    last_graph[last_info[i]].append(last_info[i + 1])
    rank[last_info[i]] = i
rank[last_info[-1]] = n

m = int(input())
change_info = [list(map(int, input().split())) for i in range(m)]

indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
for info in change_info:
    if rank[info[0]] > rank[info[1]]:
        rank[info[0]], rank[info[1]] = rank[info[1]], rank[info[0]]
        last_indegree