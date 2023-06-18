# 1966번: 프린터 큐
'''
1. popleft -> 중요도 확인
2. 더 높은 중요도 존재하면 -> append
                없다면 -> 인쇄
problem:  문서의 개수와 문서의 중요도가 주어졌을 때 각 문서가 몇 번째로 출력되는 지 알아내라
문서의 개수  N(1 ≤ N ≤ 100)
알고 싶은 문서가 큐에 놓여 있는 순서 정수  M(0 ≤ M < N) 맨 왼쪽 0번째
두 번째 줄 N개의 문서 중요도가 차례대로 (1이상 9이하) 중요도가 같을 수 있음.
'''
from collections import deque
for test_case in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append((data[i], i)) # (중요도, 처음 순서)
    cnt = 0 # 인쇄 순서
    while n > 1:
        now = q.popleft() # 큐의 맨 앞 원소
        if max(q)[0] <= now[0]: # 현재 원소의 중요도가 나머지 원소들의 중요도보다 크거나 같을때
            n -= 1 # 원소 개수 1 감소
            cnt += 1
            if now[1] == m: # 현재 원소의 처음 순서가 m이면 break
                break
            continue
        q.append(now) # 중요도가 더 큰 원소가 있다면 뒤로 가기
    # 남은 원소의 개수가 2개 이상이거나 1개이면서 남은 원소가 m이 아닐 때 cnt 출력
    # 남은 원소의 개수가 1개이고 그 원소가 m일 때 cnt + 1
    print(cnt if n > 1 or q[0][1] != m else cnt + 1)