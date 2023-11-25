import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
cards = deque()
cards.extend(range(1, n + 1, 1))

while len(cards) > 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)
print(cards[0])