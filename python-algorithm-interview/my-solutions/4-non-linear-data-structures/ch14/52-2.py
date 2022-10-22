# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            # 현재 노드가 최솟값보다 작다면, 오른쪽 재귀 결과를 리턴.
            if node.val < L:
                return dfs(node.right)
            # 현재 노드가 최댓값보다 크다면, 왼쪽 재귀 결과를 리턴.
            elif node.val > R:
                return dfs(node.left)
            # 현재 노드가 범위 내에 있다면, 다음을 리턴.
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
