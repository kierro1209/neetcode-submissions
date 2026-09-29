"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        begin = head
        equal = defaultdict(Node)
        
        while head:
            equal[head] = Node(head.val)
            head = head.next
        head = begin
       
        equal[None] = None
        while head:
            equal[head].next = equal[head.next]
            equal[head].random = equal[head.random]
            head = head.next
        return equal[begin]
