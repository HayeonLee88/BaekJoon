import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

T = int(input()) 
for test_case in range(T):
    cmd = input()
    # 커서의 왼쪽에 있는 문자를 담는 덱, 커서의 오른쪽에 있는 문자를 담는 덱
    left, right = deque(), deque()
    for c in cmd:
        if c == '<': 
            if left: # 커서의 위치가 맨 앞이 아니라면 커서 왼쪽으로 움직이기
                right.appendleft(left.pop())
        elif c == '>':
            if right: # 커서의 위치가 마지막이 아니라면 커서 오른쪽으로 움직이기
                left.append(right.popleft())
        elif c == '-':
            if left: # 커서의 위치가 맨 앞이 아니라면 커서 왼쪽 문자 지우기
                left.pop()
        else: # 알파벳이나 숫자가 입력되면 추가하기
            left.append(c)
    print(''.join(left) + ''.join(right))
    