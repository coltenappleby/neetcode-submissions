# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return None
        stack = []

        length = 0
        node = head
        while node:
            length += 1
            stack.append(node)
            node = node.next

        # could i do:
        # stack[length-n-1].next = stack[length-n+1]

        if length == n:
            return head.next
        next_node = None
        i = 0
        while stack:
            i += 1
            node = stack.pop()
            if i == n:
                node = stack.pop()
                node.next = next_node

            next_node = node
        return node