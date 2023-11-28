import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
answer = 0

for _ in range(n):
    word = input()
    stack = []
    
    if len(word) % 2 != 0:
        continue
        
    for c in word:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    if not stack:
        answer += 1
        
print(answer)
