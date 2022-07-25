# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    longest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우: 방향에 맞는 상태값 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 최종 결과: 왼쪽, 오른쪽 상태값의 합 중 글로벌 최대치
            self.longest = max(self.longest, left + right)
            # 리턴값: 자식 노드 상태값 중 큰 것
            return max(left, right)

        dfs(root)
        return self.longest
