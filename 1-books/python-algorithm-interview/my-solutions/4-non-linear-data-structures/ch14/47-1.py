from collections import deque

# 주의: 리트코드에서는 TreeNode 클래스를 지워야 정상 작동함.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        q = deque([root])
        result = []
        # BFS로 돌면서 자식 노드는 큐에 넣고, 현재 노드의 값을 결과에 추가
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == "#":
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        idx = 1

        # BFS로 돌면서, 인덱스를 활용하여 자식 정보 업데이트
        while q:
            node = q.popleft()
            if nodes[idx] != "#":
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            if nodes[idx] != "#":
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        return root
