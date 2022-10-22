# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # 높이 차이가 나는 경우 -1을 리턴하고 위로 계속 전달
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # 상태값: '현재노드에서 리프노드까지의 거리 + 1'
            return max(left, right) + 1

        return dfs(root) != -1
