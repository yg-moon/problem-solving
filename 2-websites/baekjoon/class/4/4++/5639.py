# 이진 검색 트리
# 출처1: https://imzzan.tistory.com/41
# 출처2: https://velog.io/@yujng/백준-5639번이진-검색-트리-파이썬Python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력의 개수가 정해져 있지 않으므로 try-except문 사용
arr = []
while True:
    try:
        val = int(input())
        arr.append(val)
    except:
        break

# 분할정복으로 후위순회 구하기
def postorder(start, end):
    if start > end:
        return
    mid = end + 1  # 기본값 (첫번째 값보다 큰 값이 존재하지 않을 경우를 대비)
    # 핵심: 전위순회는 첫번째 값보다 큰 값이 나올때를 기준으로 좌우 서브트리로 나뉘는 성질을 이용
    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            mid = i
            break
    postorder(start + 1, mid - 1)  # 왼쪽 서브트리에서 재귀
    postorder(mid, end)  # 오른쪽 서브트리에서 재귀
    print(arr[start])  # 자기자신을 출력


postorder(0, len(arr) - 1)

"""
- 난이도: 골드5
- 분류: 트리

요약
- 목표
    - preorder를 postorder로 바꾸기.
    - 즉, (root->left->right) 순서로 입력된 값을 (left->right->root) 순서로 출력하기.
- 방법
    - 후위순회 설계
        - left 서브트리 재귀
        - right 서브트리 재귀
        - print(root)
    - 핵심: 전위순회에서는 첫번째 값보다 큰 값이 나올때를 기준으로 좌우 서브트리로 나뉘는 성질을 이용.
        - 재귀를 통해 이 과정을 반복하면 전체가 (left->right->root) 순서로 출력된다.
"""
