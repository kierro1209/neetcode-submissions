# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow = ListNode(0, head)
        begin = head
        prev = slow
        
        while n > 0:
            begin = begin.next
            n -= 1
        
        while begin:
            prev = prev.next
            begin = begin.next
        
        prev.next = prev.next.next
        return slow.next