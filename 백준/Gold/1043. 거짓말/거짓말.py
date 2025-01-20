import sys


input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

T = data[0]
truth_knowers = data[1:] if T > 0 else []

# 각 파티 참석자 정보를 저장
parties = [list(map(int, input().split())) for _ in range(m)]


check = [False] * (n + 1)  # 1~n 사람 중 진실 아는 사람만 True
for person in truth_knowers:
    check[person] = True

party_members = []
for party in parties:
    count = party[0]
    members = party[1:]
    party_members.append(members)


if T > 0:  # 진실 아는 사람이 1명 이상 있을 때만 전파 필요
    changed = True
    while changed:
        changed = False
        for members in party_members:
            # 파티에 진실을 아는 사람이 한 명이라도 있다면
            if any(check[m] for m in members):
                for m in members:
                    if not check[m]:
                        check[m] = True
                        # 새로 진실을 알게 된 사람이 있다면, 다음 루프에서 또 검사 필요
                        changed = True


answer = 0
for members in party_members:
    # 진실 아는 사람이 1명도 없다면 거짓말
    if not any(check[m] for m in members):
        answer += 1

print(answer)