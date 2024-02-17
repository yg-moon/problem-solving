from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # preorder의 맨 앞 원소는 inorder의 분할 인덱스
            idx = inorder.index(preorder.pop(0))

            # inorder 분할 정복
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[0:idx])
            node.right = self.buildTree(preorder, inorder[idx + 1 :])

            return node
