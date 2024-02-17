from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            depth += 1
            # 큐에서 노드를 하나 뽑고, 자식들을 다시 큐에 삽입.
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        # BFS 반복 횟수 = 트리 전체 깊이
        return depth
