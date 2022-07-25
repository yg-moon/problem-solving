from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 재귀적으로, 왼쪽과 오른쪽 자식을 스왑하면 된다.
        def invert(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return

            # 임시저장
            right = node.right

            if node.left:
                node.right = invert(node.left)
            else:
                node.right = None
            if right:
                node.left = invert(right)
            else:
                node.left = None

            return node

        invert(root)
        return root
