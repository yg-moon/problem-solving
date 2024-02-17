# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced = True

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            
            # 최적화: 이미 오답이 발견된 경우 즉시 리턴
            nonlocal balanced
            if not balanced:
                return
            
            right = dfs(node.right)

            if not balanced:
                return

            if abs(left - right) > 1:
                balanced = False

            # 상태값: 현재노드에서 리프노드까지의 거리
            return max(left, right) + 1

        dfs(root)
        return balanced
