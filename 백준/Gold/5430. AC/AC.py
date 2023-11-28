import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    cmd = input()
    n = int(input())
    array = input()

    if n:
        array = list(array[1:len(array) - 1].split(','))
    else:
        array = []

    error_check = False
    reversed_check = False
    for c in cmd:
        if c == "R":
            reversed_check = not reversed_check
        else:
            if array: # 비어있는지 체크
                if reversed_check: # 뒤집혔다면
                    array.pop()
                else:
                    array.pop(0)
            else:
                error_check = True
                break

    if error_check:
        print("error")
    elif reversed_check:
        print('['+','.join(array[::-1]) + ']')
    else:
        print('['+','.join(array) + ']')
        