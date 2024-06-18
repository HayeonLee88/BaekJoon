import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

words = set(input() for _ in range(n))

sorted_words = sorted(words)
sorted_words = sorted(sorted_words, key=lambda x: len(x))

print(*sorted_words, sep='\n')