# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            
            # 높이 차이가 나는 경우 -1을 리턴하고 위로 계속 전달
            if left == -1 or \
                    right == -1 or \
                    abs(left - right) > 1:
                return -1

            # 일반적인 경우 현재 높이에 1을 더해줌
            return max(left, right) + 1

        return check(root) != -1
