import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 리턴값: 현재노드 기준 max depth
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if left - right > 1 or left - right < -1:
                self.balanced = False

            return max(left, right) + 1

        dfs(root)
        return self.balanced
