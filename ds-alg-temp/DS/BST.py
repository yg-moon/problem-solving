# BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(node):
    if node:
        inorder(node.left)
        print(node.key)
        inorder(node.right)


def search(node, key):
    if not node or node.key == key:
        return node
    # 찾으려는 값이 더 작으면 왼쪽, 더 크면 오른쪽으로 내려감 (재귀적으로)
    if key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


def insert(node, key):
    # 빈 트리의 경우 새로운 노드를 리턴
    if not node:
        return Node(key)
    # 삽입하려는 값이 더 작으면 왼쪽 서브트리에서 재귀
    if key < node.key:
        node.left = insert(node.left, key)
    # 삽입하려는 값이 더 크면 오른쪽 서브트리에서 재귀
    else:
        node.right = insert(node.right, key)
    # 입력으로 받은 (루트)노드를 그대로 리턴
    return node


def min_val(node):
    cur = node
    # 왼쪽 끝까지 내려가서 가장 작은 노드를 찾음
    while cur.left:
        cur = cur.left
    return cur


def delete(node, key):
    # Base Case
    if not node:
        return node
    # 삭제하려는 값이 더 작으면 왼쪽 서브트리에서 재귀
    if key < node.key:
        node.left = delete(node.left, key)
    # 삭제하려는 값이 더 크면 오른쪽 서브트리에서 재귀
    elif key > node.key:
        node.right = delete(node.right, key)
    # 값이 일치하면 현재 노드를 삭제
    else:
        # 자식이 1개 또는 0개인 경우
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # 자식이 2개인 경우
        # Get the inorder successor (smallest in the right subtree)
        temp = min_val(node.right)
        # Copy the inorder successor's content to current node
        node.key = temp.key
        # Delete the inorder successor
        node.right = delete(node.right, temp.key)

    # 입력으로 받은 (루트)노드를 그대로 리턴
    return node


# Driver code
""" 
Let's create the following BST
		  50
		/	 \
	  30	 70
      / \    / \
	20  40  60  80
"""
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)
print()

print("Delete 20")
root = delete(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
print()

print("Delete 30")
root = delete(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
print()

print("Delete 50")
root = delete(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)
print()

# 원본 출처: https://www.geeksforgeeks.org/deletion-in-binary-search-tree/
