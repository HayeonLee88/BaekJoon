import sys


input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())


class Node(object):
    def __init__(self):
        self.children = dict()
        self.has_end = False


class Trie(object):
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.has_end = True

    def starts_with(self, prefix):
        curr_node = self.head
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True


set_s = [input() for _ in range(n)]
check = [input() for _ in range(m)]

trie = Trie()

for word in set_s:
    trie.insert(word)

answer = 0
for word in check:
    if trie.starts_with(word):
        answer += 1

print(answer)