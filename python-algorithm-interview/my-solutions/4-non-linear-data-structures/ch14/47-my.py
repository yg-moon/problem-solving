from collections import deque

# 주의: 리트코드에서는 TreeNode 클래스를 지워야 정상 작동함.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        # 예외처리
        if not root:
            return ""

        q = deque([root])
        encoded_list = []

        # BFS
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                encoded_list.append(str(node.val))
            else:
                encoded_list.append("null")

        # 리프노드의 null 자식표현 지우기
        while encoded_list[-1] == "null":
            encoded_list.pop()

        return " ".join(encoded_list)

    def deserialize(self, data: str) -> TreeNode:
        # 예외처리
        if data == "":
            return None

        # data를 TreeNode의 리스트로 변환
        tree_nodes = data.split()
        for i, val in enumerate(tree_nodes):
            if val == "null":
                tree_nodes[i] = None
            else:
                tree_nodes[i] = TreeNode(int(val))

        # idx 정보를 함께 묶어줌
        tree_nodes = list(zip(range(len(tree_nodes)), tree_nodes))

        # 큐 2개 활용
        # - 큐1: 원래처럼 BFS
        # - 큐2: 자식 노드 두 개를 임시보관
        q1 = deque([tree_nodes[0]])
        q2 = deque()

        # 자식 정보 업데이트: BFS + 자식 목록 관리
        while q1:
            idx, node = q1.popleft()

            # 자식들을 두 큐에 삽입
            if 2 * idx + 1 < len(tree_nodes):
                i, left = tree_nodes[2 * idx + 1]
                q1.append((i, left))
                q2.append(left)
            if 2 * idx + 2 < len(tree_nodes):
                i, right = tree_nodes[2 * idx + 2]
                q1.append((i, right))
                q2.append(right)

            # 현재 노드가 null이 아니라면 자식 정보 업데이트
            if node:
                if q2:
                    node.left = q2.popleft()
                if q2:
                    node.right = q2.popleft()

        return tree_nodes[0][1]
