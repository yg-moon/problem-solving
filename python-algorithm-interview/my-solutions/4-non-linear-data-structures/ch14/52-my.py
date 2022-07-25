from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum: int = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root and root.val >= low and root.val <= high:
            self.sum += root.val
        if root.left:
            self.rangeSumBST(root.left, low, high)
        if root.right:
            self.rangeSumBST(root.right, low, high)
        return self.sum
