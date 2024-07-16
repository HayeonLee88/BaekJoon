import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()
wheels = {}
for i in range(1, 5):
    wheels[i] = deque(map(int, list(input())))

state = []
def rotate(start, end, dir1, dir2): 
    '''
    num: 기준이 되는 톱니바퀴 번호
    dir1: -1 이면 왼쪽 1이면 오른쪽 방향 톱니 탐색
    dir2: 톱니가 돌아갈 방향
    '''
    global state
    d = dir2
    for i in range(start, end, dir1):
        d *= -1
        if dir1 == 1:
            if state[i + dir1 * -1] == 1:
                wheels[i].rotate(d)
            else:
                break
        else:
            if state[i] == 1:
               wheels[i].rotate(d)
            else:
                break
        
n = int(input())
answer = 0
for i in range(n):
    state = [-1, wheels[1][2] + wheels[2][-2], wheels[2][2] + wheels[3][-2], wheels[3][2] + wheels[4][-2]]
    num, dir = map(int, input().split())
    wheels[num].rotate(dir)
    rotate(num -1, 0, -1, dir)
    rotate(num + 1, 5, 1, dir)

for j in range(4):
     if wheels[j + 1][0] == 1:
        answer += 2 ** j
                   
print(answer)