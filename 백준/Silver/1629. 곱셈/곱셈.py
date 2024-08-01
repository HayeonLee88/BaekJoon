import sys
sys.setrecursionlimit(100000)
a, b, c = map(int, input().split())


def divide_conquer(num, times):
    if times == 1:
        return num % c
    else:
        if times % 2 == 0:
            intermediate = divide_conquer(num, times // 2) % c
            return intermediate * intermediate % c
        else:
            intermediate = divide_conquer(num, times // 2) % c
            return intermediate * intermediate * num % c
print(divide_conquer(a, b) % c)