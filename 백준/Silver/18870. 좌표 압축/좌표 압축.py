import sys

input = lambda:sys.stdin.readline().rstrip()

n = int(input())
points = list(map(int, input().split()))
sorted_points = sorted(set(points))
compressed_points = dict()
cnt = 0
for point in sorted_points:
    compressed_points[point] = cnt
    cnt += 1

for point in points:
    print(compressed_points[point], end=' ')
