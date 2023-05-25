# 1181번: 단어 정렬
import sys
n = int(input())
words = list({sys.stdin.readline().rstrip() for _ in range(n)})
words.sort() # 알파벳 순으로 정렬 후
words.sort(key=lambda x: len(x)) # 단어 길이 순으로 정렬
for word in words:
    print(word)