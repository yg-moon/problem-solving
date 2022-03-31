from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            next = head.next # 1.next 저장
            head.next = prev # 2.prev 왼쪽에 하나 더 달기
            prev = head # 3.prev 정보 최신화
            head = next # 4.다음 칸으로 이동
        
        return prev


# while문 내부를 다중할당으로 쓰면 헷갈리길래 줄을 분리했다.
