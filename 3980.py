# 3980번: 선발 명당 (DFS, BackTracking)
'''
11명의 선수 각각의 포지션에서의 능력을 0부터 100까지의 정수로 나타냄
모든 선수의 포지션을 정하는 프로그램을 작성
단, 모든 포지션에 선수를 배치해야 하고, 각 선수는 능력치가 0인 포지션에 배치될 수 없다.

problem: 각 테스트 케이스에 대해, 모든 포지션의 선수를 채웠을 때, 능력치의 합의 최댓값을 출력. 항상 하나 이상의 올바른 라인업을 만들 수 있다.

How?
    깊이우선 탐색, 백트래킹을 활용해
'''
import sys

input = lambda: sys.stdin.readline().rstrip()

c = int(input())


def BackTracking(cnt, score):
    global answer
    if cnt == 11:
        answer = max(answer, score)
        return True
    else:
        for i in range(11):
            if position[i] or lineup_info[cnt][i] == 0:  # i번째 포지션이 정해졌거나, cnt 번째 선수의 i 포지션 능력치가 0이면 continue
                continue
            position[i] = 1  # 포지션 확정
            info[i] = lineup_info[cnt][i]
            BackTracking(cnt + 1, score + lineup_info[cnt][i])  # 다음 포지션 정하기, 포지션 능력치 더해 넘기기
            position[i] = 0


for _ in range(c):
    answer = 0
    # 라인업에 선발된 선수들의 포지션 별 능력치 정보
    lineup_info = [list(map(int, input().split())) for _ in range(11)]
    position = [0] * 11  # 포지션 유뮤 리스트 초기화
    info = [0] * 11
    BackTracking(0, 0) # 첫 시작을 0번째~10번째 선수까지 모든 순서대로로
    print(answer)