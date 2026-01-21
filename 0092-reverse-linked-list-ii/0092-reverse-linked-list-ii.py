# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: #edge case
            return head
        p = None
        c = r  = head
        start = None # to handle edge case
        i = 0
        while i != left-1:
            start = c
            c = c.next
            i +=1
        tail = c
        
        i = 0 
        while i!= right-left+1:
            n = c.next
            c.next = p
            p = c
            c = n
            i +=1

        if start:
            start.next = p
        else:
            head = p
        tail.next = c
        
        return head 
