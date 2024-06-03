import sys

input = lambda: sys.stdin.readlines()
tmp = -1 # 한 줄의 글자 길이
words = []

lines = input()
for line in lines:
    words += line.split()

output = []
for word in words:
    if word == "<br>":
        print(" ".join(output))
        output = []
        tmp = -1
        continue
    elif word == "<hr>":
        if output:
            print(" ".join(output))
        print("-" * 80)
        output = []
        tmp = -1
        continue
    tmp += (len(word) + 1)

    if tmp > 80:
        print(" ".join(output))
        output = [word]
        tmp = len(word)
        continue
    output.append(word)

if output:
    print(" ".join(output))