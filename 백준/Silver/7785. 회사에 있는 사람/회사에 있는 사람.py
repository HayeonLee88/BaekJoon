import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
names = dict()

for i in range(n):
    name, log = input().split()
    names[name] = log
    
names = sorted(names.items(), reverse=True)
for name, log in names:
    if log == 'enter':
        print(name)