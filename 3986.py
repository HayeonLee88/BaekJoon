# 3986 좋은 단어

n = int(input())
answer = 0
for i in range(n):
    word = input()
    if len(word) % 2 != 0:
        continue
    l = list(word[0])
    for j in range(1, len(word)):
        l.append(word[j])
        print(l)
        tail = l[-2:]
        if tail == ['B', 'B'] or tail == ['A', 'A']:
            l.pop()
            l.pop()
    if len(l) == 0:
        answer += 1
print(answer)