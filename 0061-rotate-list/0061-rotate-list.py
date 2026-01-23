# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        length = 0
        while fast.next:
            fast = fast.next
            length += 1

        k = k%length
        fast = dummy
        for i in range(k%length):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = dummy.next
        n = slow.next
        slow.next = None

        return n
        
        