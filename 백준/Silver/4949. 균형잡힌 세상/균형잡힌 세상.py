import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    string = input()
    if string == '.':
        break
    stack = list()
    answer = "yes"
    for c in string:
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                answer = "no"
                break
            else:
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                answer = "no"
                break
            else:
                stack.pop()
    if stack:
        answer = "no"
    print(answer)
    