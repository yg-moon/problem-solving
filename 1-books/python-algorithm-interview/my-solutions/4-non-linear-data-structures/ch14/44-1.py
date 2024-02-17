# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longest_path = 0

        def dfs(node):
            nonlocal longest_path
            if not node:
                return 0
            # 좌우로 끝까지 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            # 핵심: 현재 노드와 자식 노드의 값을 비교해서, left 또는 right 값을 수정
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            # 가장 긴 동일값 경로
            longest_path = max(longest_path, left + right)
            # 상태값: 리프 노드에서 현재 노드까지 max_univalue_path의 길이.
            return max(left, right)

        dfs(root)
        return longest_path
