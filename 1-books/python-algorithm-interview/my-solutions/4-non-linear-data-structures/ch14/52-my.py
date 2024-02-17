from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        def helper(root: Optional[TreeNode]) -> None:
            if not root:
                return
            # 범위 안에 있다면 값을 더해주기
            nonlocal answer
            if low <= root.val <= high:
                answer += root.val
            # 범위 안에 있는 노드만 방문하기
            if root.val > low:
                helper(root.left)
            if root.val < high:
                helper(root.right)

        helper(root)
        return answer
