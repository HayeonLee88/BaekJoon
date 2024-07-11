import sys
input = lambda:sys.stdin.readline().rstrip()

k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]
wires.sort(reverse = True)

start = 1
end = wires[0] # 가장 짧은 길이의 랜선
answer = 1

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    check = False
    for wire in wires:
        tmp += (wire // mid)
        if tmp >= n:
            answer = max(answer, mid)
            check = True
            start = mid + 1
            break
    if not check:
        end = mid - 1

print(answer)