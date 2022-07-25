from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # 예외처리
        if not root1:
            return root2
        if not root2:
            return root1
        
        # root1에 합치기
        def dfs(
            root1: Optional[TreeNode], root2: Optional[TreeNode]
        ) -> Optional[TreeNode]:
            # 자식이 다 있으면 재귀
            if root1.left and root2.left:
                root1.left = dfs(root1.left, root2.left)
            if root1.right and root2.right:
                root1.right = dfs(root1.right, root2.right)

            # 자식이 없으면 옆 트리꺼 가져오기
            if not root1.left:
                root1.left = root2.left
            if not root1.right:
                root1.right = root2.right

            root1.val += root2.val
            
            # 재귀 리턴값: 현재까지 머지 완료된 서브트리의 루트
            return root1

        return dfs(root1, root2)
