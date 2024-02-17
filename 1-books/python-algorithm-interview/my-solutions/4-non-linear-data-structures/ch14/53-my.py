from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []

        def helper(root):
            if not root:
                return
            nodes.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        nodes.sort()

        answer = int(1e9)
        for i in range(1, len(nodes)):
            answer = min(answer, nodes[i] - nodes[i - 1])
        return answer


"""
브루트포스. 모든 값을 리스트에 넣고, 정렬해서, 인접한 값들의 차를 계산하여 최소를 리턴.
"""
