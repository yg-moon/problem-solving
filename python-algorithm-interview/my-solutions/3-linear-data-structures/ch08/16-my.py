from typing import List, Optional
from unittest import result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list1 = []
        list2 = []

        # Convert linked list to Python list
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        # Calculate answer
        num1 = int("".join(str(x) for x in list1[::-1]))
        num2 = int("".join(str(x) for x in list2[::-1]))
        sum = num1 + num2
        result_list = [int(x) for x in str(sum)][::-1]

        # Convert Python list to linked list
        root = head = ListNode(None)
        for i in range(len(result_list)):
            head.val = result_list[i]
            if i != len(result_list) - 1:
                head.next = ListNode(None)
                head = head.next

        return root
