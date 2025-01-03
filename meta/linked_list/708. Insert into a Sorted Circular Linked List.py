
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    O(n)
    O(1)
    """
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        prev, curr = head, head.next
        while curr != head:
            if prev.val <= insertVal <= curr.val or (
                prev.val > curr.val and \
                (insertVal >= prev.val or insertVal <= curr.val)
            ):
                break
            prev, curr = curr, curr.next
        prev.next = node
        node.next = curr
        return head

head = [3,4,1]; insertVal = 2 # res [3,4,1,2]

