p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))

def ccw(p1, p2, p3):
    cross = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if cross > 0:
        return 1
    elif cross < 0:
        return -1
    else:
        return 0

print(ccw(p1, p2, p3))