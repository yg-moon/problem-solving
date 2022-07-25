import collections

# 주의: 리트코드에서 이거 주석 풀면 오류남.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 예외처리
        if not root:
            return ""

        queue = collections.deque([root])
        encoded_list = []

        # BFS
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                encoded_list.append(str(node.val))
            else:
                encoded_list.append("null")

        # 리프노드의 null 자식표현 지우기
        while encoded_list[-1] == "null":
            encoded_list.pop()

        return " ".join(encoded_list)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
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
        queue = collections.deque([tree_nodes[0]])
        child_queue = collections.deque()

        # 자식 정보 업데이트: BFS + 자식 목록 관리
        while queue:
            idx, node = queue.popleft()

            # 자식들을 두 큐에 삽입
            if 2 * idx + 1 < len(tree_nodes):
                i, left = tree_nodes[2 * idx + 1]
                queue.append((i, left))
                child_queue.append(left)
            if 2 * idx + 2 < len(tree_nodes):
                i, right = tree_nodes[2 * idx + 2]
                queue.append((i, right))
                child_queue.append(right)

            # null 노드가 아니라면 자식 정보 업데이트
            if node:
                if child_queue:
                    left = child_queue.popleft()
                else:
                    left = None
                if child_queue:
                    right = child_queue.popleft()
                else:
                    right = None
                node.left = left
                node.right = right

        return tree_nodes[0][1]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# - serialize
#     - 목표: 트리를 표현식으로 만들기.
#     - 리스트로 만들고, 마지막에 공백 넣어서 join.
#     - 방법: BFS
#     - 리프노드의 자식 지우기: 맨 뒤에 trailing null 다 지우기.

# - deserialize
#     - 목표: 표현식을 트리로 만들기.
#     - 2n+1, 2n+2 기준으로 left, right 설정해주기.
#     - 직렬화도 BFS. 그럼 역도 BFS? 맞는듯!
#     - 큐 2개 버전
#       - 큐1: 원래처럼 BFS
#       - 큐2: 자식만 받고, 매번 빼내기. (큐에 내용이 있으면 그걸로 달고, 없으면 None 달기)
