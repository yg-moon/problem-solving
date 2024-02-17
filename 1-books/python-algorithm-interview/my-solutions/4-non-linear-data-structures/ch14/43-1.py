# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            # 기본 케이스
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            # 트리 직경
            diameter = max(diameter, left + right + 2)
            # 상태값: 리프 노드에서 현재 노드까지의 거리
            return max(left, right) + 1

        dfs(root)
        return diameter
