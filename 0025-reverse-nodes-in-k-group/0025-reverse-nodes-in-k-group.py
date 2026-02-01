# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        gprev = dummy
        p = None
        
        while True:
            kth = gprev
            for _ in range(k):
                if not kth.next:
                    return dummy.next
                kth = kth.next
            
            gnext = kth.next
            
            c = gprev.next
            p = gnext
            for _ in range(k):
                n = c.next
                c.next = p
                p = c
                c = n
            
            temp = gprev.next
            gprev.next = kth
            gprev = temp
            
        return dummy.next
            
