# 1920번: 수 찾기
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
m = int(input())
B = list(map(int, sys.stdin.readline().rstrip().split()))

for b in B:
    start = 0
    end = n - 1
    check = False
    while start <= end:
        mid = (start + end) // 2
        search = A[mid]
        if search > b:
            end = mid - 1
        elif search < b:
            start = mid + 1
        else:
            check = True
            break
    print(1 if check else 0)
