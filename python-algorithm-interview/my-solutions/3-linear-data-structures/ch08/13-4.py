from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        
        # Runner implementation
        # Create 'rev', a reversed list for the first half
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        # If length is odd number, skip one more time
        if fast:
            slow = slow.next

        # Compare rev and the second half
        while rev:
            if rev.val == slow.val:
                rev, slow = rev.next, slow.next
            else:
                return False
        
        return True


# Run code
# sample_input1 = ListNode(1,ListNode(2,ListNode(2,ListNode(1)))) # [1,2,2,1]
# sample_input2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4)))) # [1,2,3,4]
# print(Solution().isPalindrome(sample_input1)) # True
# print(Solution().isPalindrome(sample_input2)) # False

### Time Complexity
# 순서대로 한번 쭉 훑으므로 O(n).

### Note
# 
