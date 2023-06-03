# 5052번: 전화번호 목록
# 정렬의 의미를 생각해보기

import sys
input = lambda :sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    n = int(input())
    data = [input() for _ in range(n)]
    data.sort() # 오름차순 정렬을 하면 제일 비슷한 번호가 바로 옆에 있다.
    for j in range(n - 1):
        if data[j] == data[j+1][:len(data[j])]:
            print("NO")
            break
    else:
        print("YES")