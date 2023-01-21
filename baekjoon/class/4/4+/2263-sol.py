# 트리의 순회
# 출처1: https://ku-hug.tistory.com/135?category=978336
# 출처2: https://velog.io/@bae_mung/Python-BOJ-2263-트리의-순회
import sys

sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 중위순회 결과의 인덱스값을 저장
# (이유: 후위순회의 끝값이 중위순회의 어디 인덱스에 위치한지 확인하기 위해)
in_idx = [0] * (n + 1)
for i in range(n):
    in_idx[inorder[i]] = i

# 분할정복으로 전위순회 구하기
def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료조건
    if (in_start > in_end) or (post_start > post_end):
        return

    # 후위순회의 끝값이 각 서브트리의 루트임을 이용
    root = postorder[post_end]
    # 중위순회는 루트의 좌우로 서브트리가 갈라지는 성질을 이용
    left = in_idx[root] - in_start  # 왼쪽 서브트리의 노드 수
    right = in_end - in_idx[root]  # 오른쪽 서브트리의 노드 수

    # 현재 루트 출력
    print(root, end=" ")
    # 왼쪽 서브트리에 대해 재귀 (중위순회, 후위순회 범위 조정)
    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # 오른쪽 서브트리에 대해 재귀 (중위순회, 후위순회 범위 조정)
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)


# 중위순회, 후위순회 모두 0부터 n-1(전체 범위)값을 주고 전위순회를 구함
preorder(0, n - 1, 0, n - 1)

"""
- 난이도: 골드2
- 분류: 트리

요약
- 전위순회 설계
    - print(root)
    - left 서브트리 재귀
    - right 서브트리 재귀 
- 핵심
    - 후위순회의 끝값이 각 서브트리의 루트임을 이용
    - 중위순회에서 루트의 좌우로 서브트리가 갈라지는 성질을 이용
    - 왼쪽, 오른쪽 서브트리에서 재귀할때 중위순회, 후위순회의 범위 조정

관련 문제
- BOJ #5639
    - 개요: preorder를 postorder로 바꾸는 문제.
    - 해법: 후위순회 설계, 분할정복을 이용해 서브트리 탐색범위를 조정하며 찾는 과정이 상당부분 유사함.
- Leetcode #105
    - 개요: preorder와 inorder가 주어졌을때, 트리 전체를 구하는 문제.
    - 해법: preorder의 첫번째 값은 inorder의 중앙분리대 역할을 한다. (따라서 inorder를 분할정복)
"""
