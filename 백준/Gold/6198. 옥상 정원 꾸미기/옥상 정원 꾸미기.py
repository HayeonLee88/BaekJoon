import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
buildings = [int(input()) for _ in range(n)]

n -= 1
answer = 0
stack = [[0, 0]] # i번 ~ n번 빌딩까지 i번 빌딩보다 높거나 같은 [빌딩의 높이와, 위치]를 저장하는 스택

for i in range(n, -1, -1):
    building = buildings[i]
    while stack and stack[-1][0] < building: # 현재 빌딩 앞에 더 높거나 같은 높이인 빌딩이 있는지 탐색
        stack.pop() # 앞에 있는 빌딩의 높이가 작다면 pop
    if stack: # 현재 빌딩보다 높거나 같은 빌딩이 앞에 있다면
        answer += (stack[-1][1] - i - 1) # 현재 빌딩과 높거나 같은 빌딩 사이의 빌딩의 수 구하기 
    else:
        answer += (n - i) # 현재 빌딩의 위치에서 보이는 모든 빌딩의 수 = 끝에 위치한 빌딩부터 현재 위치의 바로 앞 빌딩까지 
    stack.append([building, i]) # 스택에 현재 빌딩의 높이와 위치 담기
    
print(answer)
