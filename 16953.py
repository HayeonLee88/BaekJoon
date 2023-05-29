# 16953번: A -> B
A, B = map(int, input().split())
answer = 1
while B > A: # A에서 B로 되는 과정에 가능한 숫자는 일의 자리가 1인 경우와 짝수인 경우 뿐인다.
    if B % 10 == 1:
        B = (B - 1) // 10
    elif B % 2 == 0:
        B //= 2
    else:
        break
    answer += 1
if B == A:
    print(answer)
else:
    print(-1)