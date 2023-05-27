# 2630번: 색종이 만들기
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
paper = []
white = blue = 0
for i in range(n):
    paper.append(list(map(int, input().split())))


def cutting_paper(x, y, width):
    global white, blue
    if width < 1:
        return False
    if paper[x][y]:
        color = 1
    else:
        color = 0
    for i in range(width):
        for j in range(width):
            if paper[x + i][y + j] != color:
                new_w = width // 2
                cutting_paper(x, y, new_w)
                cutting_paper(x + new_w, y, new_w)
                cutting_paper(x, y + new_w, new_w)
                cutting_paper(x + new_w, y + new_w, new_w)
                return False
    if paper[x][y]:
        blue += 1
    else:
        white += 1
    return True


cutting_paper(0, 0, n)
print(f'{white}\n{blue}')
