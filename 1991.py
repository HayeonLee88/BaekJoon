# 1991번: 트리 순회
n = int(input())
graph = []

for i in range(n):
    graph.append(input().split())


class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


tree = {}
for item, left, right in graph:
    tree[item] = Node(item, left, right)


def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
    return 0


def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])
    return 0


def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')
    return 0


preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
