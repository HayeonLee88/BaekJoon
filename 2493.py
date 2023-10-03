# 2493번: 탑(Stack)
'''
problem? 탑들의 개수 N과 탑들의 높이가 주어질 때, (N: 1 이상 500,000 이하, 탑 높이: 1 이상 100,000,000 이하)
각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내내라. 수신 가능한 탑이 없을 경우 0 출력

(cf.뒤의 탑부터 탐색하면 그 탑보다 앞에 있는 모든 탑을 탐색 X)

How? 앞의 탑부터 탐색하여 해당 위치에서 제일 높은 탑만 stack에 저장힌다.
     1. stack이 안 비어 있다면 stack 가장 위 탑의 높이를 현재 탑의 높이와 비교한다.
     2. 현재 탑보다 높거나 같으면 answer에 stack의 제일 위에 있는 탑 위치 저장 후, stack에 (현재 탑 인덱스 + 1, 높이) 저장
     3. 만약 현재 탑이 더 높다면 2.가 될때까지 pop
     4. stack이 비었다면 (0, 0)을 담고,  answer에 0 저장한 후 stack에 (현재 탑 인덱스 + 1, 높이) 저장

stack: 레이저를 발사하는 탑보다 높이가 더 높거나 같은 가장 왼쪽 탑의 위치와 높이를 담는다
answer: 레이저를 수신하는 탑의 위치를 담는 리스트
'''
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
top_heights = list(map(int, input().split())) # 탑의 높이를 담는 리스트 초기화
stack = [] # 탑색 하는 탑의 위치에서 가장 높은 탑의 위치와 높이를 담는 스택

answer = [] # 정답 리스트 초기화
for i, h in enumerate(top_heights): # 맨 앞부터 탐색
    while stack: # 스택이 빌 동안
        if stack[-1][1] >= h: # 스택의 가장 위 탑의 높이가 현재 탑 높이보다 높거나 같다면
            answer.append(stack[-1][0] + 1) # 정답에 스택의 가장 위 탑 위치 저장
            stack.append((i, h)) # 현재 탑의 위치과 높이 스택에 저장
            break
        else: # 스택의 가장 위 탑의 높이가 현재 탑 높이보다 낮다면 높거나 같은 높이의 탑이 있을 때까지 pop
            stack.pop()
    if not stack: # 스택이 비었다면
        stack.append((0, 0)) # 수신할 탑이 없기 때문에 (0, 0) 추가
        answer.append(0) # 수신할 탑이 없음
        stack.append((i, h)) # 현재 탑의 위치과 높이 스택에 저장

print(*answer)