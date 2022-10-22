import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        # 반복구조 Inorder traversal (왼쪽 - 자신 - 오른쪽)
        while stack or node:
            # 자신을 스택에 append 하고, 왼쪽이 동날때까지 전부 스택에 append.
            while node:
                stack.append(node)
                node = node.left

            # 스택에서 하나 pop 해서, 결과 계산하고, 이전 값 정보 업데이트.
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val

            # 꺼낸 노드의 right를 다음 노드로 설정.
            node = node.right

        return result
