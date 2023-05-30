# 1759번: 암호 만들기
# 서로 다른 l개의 알파벳, 최소 1개의 모음(a, e, i, o, u)
# 최소 2개 자음, 알파벳 오름차순
from itertools import combinations

l, c = map(int, input().split())
data = list(input().split())
data.sort()
vowels = ['a', 'e', 'i', 'o', 'u']

passwords = list(combinations(data, l))

for password in passwords:
    v_cnt = 0
    c_cnt = 0
    for alpha in password:
        if alpha in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt >= 1 and c_cnt >= 2:
        print(''.join(a for a in password))
