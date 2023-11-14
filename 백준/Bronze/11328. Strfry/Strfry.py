import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for test_case in range(T):
    s1, s2 = map(list, input().split())
    s1.sort()
    s2.sort()
    if s1 == s2:
        print('Possible')
    else:
        print('Impossible')
        