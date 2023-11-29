import sys

input = lambda: sys.stdin.readline().rstrip()

string = input()
answer = 0
sticks = []

for idx, c in enumerate(string):
    if c == "(": # 쇠막대 시작 and 레이저 시작
        answer += 1
        sticks.append(idx)
    else:
        if sticks[-1] + 1 == idx: # 이전 열림 괄호가 레이저 였을 때
            answer -= 1 
            answer += (len(sticks) - 1)
        sticks.pop()

print(answer)
