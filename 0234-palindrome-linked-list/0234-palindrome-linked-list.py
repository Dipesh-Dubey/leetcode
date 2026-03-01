# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        s = f = head
        
        # FIXED CONDITION
        while f.next and f.next.next:
            f = f.next.next
            s = s.next

        c = s.next
        s.next = None

        p = None
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt

        c1 = head
        while p:
            if c1.val != p.val:
                return False
            c1 = c1.next
            p = p.next

        return True