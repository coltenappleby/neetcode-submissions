# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next == None:
            return
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        half_node = head
        half = length // 2
        while half > 0:
            half -= 1
            half_node = half_node.next

        half_node_claude = half_node.next
        half_node.next = None

        half_node_claude = self.reverse(half_node_claude)

        res = head

        p1 = None
        p2 = None
        while half_node_claude:
            p1 = head.next
            p2 = half_node_claude.next
            head.next = half_node_claude
            half_node_claude = p2
            head = head.next
            head.next = p1
            head = head.next
            length -=1
   
        

    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        