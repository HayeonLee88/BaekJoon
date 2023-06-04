# 9935번: 문자열 폭발
import sys
input = lambda:sys.stdin.readline().rstrip()
string = input()
tnt = list(input())
tnt_len = len(tnt)
stack = list(string[:tnt_len-1])

for i in range(tnt_len -1 , len(string)):
  stack.append(string[i])
  if stack[-tnt_len:] == tnt:
    for j in range(tnt_len):
      stack.pop()

print(''.join(s for s in stack) if len(stack) != 0 else 'FRULA')