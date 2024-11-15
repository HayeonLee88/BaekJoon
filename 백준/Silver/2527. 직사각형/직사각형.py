def search(a, b):
    if a[2] < b[0] or a[3] < b[1] or a[0] > b[2] or a[1] > b[3]:
        return 'd'
    elif (a[2] == b[0] and a[3] == b[1]) or (a[0] == b[2] and a[1] == b[3]) or (a[2] == b[0] and a[1] == b[3]) or (a[0] == b[2] and a[3] == b[1]):
        return 'c'
    elif (a[2] == b[0] or a[0] == b[2]) and (a[1] < b[3] and a[3] > b[1]) or (a[3] == b[1] or a[1] == b[3]) and (a[0] < b[2] and a[2] > b[0]):
        return 'b'
    else:
        return 'a'

for _ in range(4):
    x, y, p, q, a, b, l, m = map(int, input().split())
    s1 = [x, y, p, q]
    s2 = [a, b, l, m]

    print(search(s1, s2)) 