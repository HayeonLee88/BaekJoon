# 10808번: 알파벳 개수
alphabet = [0] * 26
for c in sorted(input()):
  print(c)
  alphabet[ord(c)-97] += 1
print(' '.join(str(n) for n in alphabet))
