import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    cmd = input()
    n = int(input())
    array = input()

    if n < cmd.count('D'): # 배열의 원소 개수보다 버리는 개수가 더 많은 때
        print("error")

    else:
        if n: # 원소의 개수가 0이 아니라면
            array = list(array[1:len(array) - 1].split(','))

            reversed_check = False
            for c in cmd:
                if c == "R":
                    reversed_check = not reversed_check
                else:
                    if array:  # 비어있는지 체크
                        if reversed_check:  # 뒤집혔다면
                            array.pop()
                        else:
                            array.pop(0)

            if reversed_check:
                print('[' + ','.join(array[::-1]) + ']')
            else:
                print('[' + ','.join(array) + ']')

        else: # 원소의 개수가 0이라면
            print('[]')
            