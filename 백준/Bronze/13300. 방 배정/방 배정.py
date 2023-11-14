import sys

input = lambda: sys.stdin.readline().rstrip()

total_students, max_num = map(int, input().split())
students = [[0, 0] for _ in range(7)]

for i in range(total_students):
    gender, grade = map(int, input().split())
    students[grade][gender] += 1

answer = 0
for girl, boy in students:
    answer += girl // max_num + boy // max_num
    if girl % max_num:
        answer += 1
    if boy % max_num:
        answer += 1

print(answer)