# 18112번: 이진수 게임(bfs)
'''
L: ‘시작 이진수’, K:‘목표 이진수’가 주어진다. (1 ≤ L, K ≤ 10)

    1. 한 자리 숫자를 보수로 바꾸기. 단, 맨 앞 숫자(Most Significant Digit)는 바꿀 수 없다.
    101(2) → 111(2)
    2. 현재 수에 1 더하기.
    11(2) → 100(2)
    3. 현재 수에서 1 빼기. 단, 현재 수가 0이라면 빼기가 불가능하다.
    110(2) → 101(2)

problem: ‘시작 이진수’를 ‘목표 이진수’로 만들기 위한 최소 동작 횟수를 출력

How?
    1. 이진수를 십진수로 변환하기
    2. 한 자리 숫자를 보수로 바꾸기 => xor 연산, 나머지 연산은 단순 계산

tips:
    - 시간초과 => 이미 탐색한 숫자인지 아닌지 확인하기
    - 첫자리수는 xor하면 X
    - IndexError => visited 범위 내의 숫자를 벗어날 때 try~except
'''
# 4:18~
from collections import deque

start = int(input(), 2)
target = int(input(), 2)
visited = [False] * 2048

def dfs(s, t):
    q = deque()
    q.append((s, 0))
    visited[s] = True

    def check_and_append(x, c):
        try:
            if not visited[x]:
                visited[x] = True
                q.append((x, c + 1))
        except IndexError:
            pass
    while q:
        now, cnt = q.popleft()
        if now == t:
            return cnt
        len_xor = len(bin(now)) - 3
        for i in range(0, len_xor):  # i번째 자리 숫자 바꾸기
            new = now ^ 2 ** i
            check_and_append(new, cnt)
        if now:  # 1 빼기
            new = now - 1
            check_and_append(new, cnt)
        # 1 더하기
        new = now + 1
        check_and_append(new, cnt)


answer = dfs(start, target)
print(answer)
