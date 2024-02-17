# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    new_val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위순회 순서로 노드의 값을 누적
        if root:
            self.bstToGst(root.right)
            self.new_val += root.val
            root.val = self.new_val
            self.bstToGst(root.left)
        return root
