import sys
from collections import deque


input = lambda:sys.stdin.readline().rstrip()

T = int(input())

for test_case in range(T):
    cmd = input()
    n = int(input())
    array = deque(input()[1:-1].split(','))

    # 배열의 길이보다 연산 'D'가 많을 때
    if n < cmd.count('D'):
        print('error')
    else:
        reversed = False
        for x in cmd:
            if x == 'R':
                reversed = not reversed
            else:
                # 비어 있지 않을 때
                if array:
                    # 뒤집혔다면
                    if reversed:
                        array.pop()
                    # 뒤집히지 않았다면
                    else:
                        array.popleft()
                else:
                    array = 'error'
                    break
        if array == 'error':
            print(array)
        else:
            print('['+ ','.join(list(array)[::-1]) +']' if reversed else '['+ ','.join(array) +']')