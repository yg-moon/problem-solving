# BFS 버전
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root
