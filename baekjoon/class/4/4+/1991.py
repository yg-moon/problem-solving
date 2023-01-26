# 트리 순회
# 출처: https://velog.io/@ohk9134/백준-1991번-트리-순회-python-트리-구현
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

# self -> left -> right
def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


# left -> self -> right
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


# left -> right -> self
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")

"""
- 난이도: 실버1
- 분류: 트리

배운점
- 트리 구조는 dict를 통해 {root: [left, right]} 형태로 저장할 수 있다.
- 보통은 2차원 배열로 저장하고, 노드가 문자일 경우 dict를 쓰면 될 듯.
"""
