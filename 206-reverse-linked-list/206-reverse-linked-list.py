# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return head
        start= head
        nodes = []
        while start : 
            nodes.append(start)
            start = start.next
        dummy_node = ListNode()
        start = nodes.pop()
        dummy_node.next = start
        while nodes :
            start.next = nodes.pop()
            start = start.next
        start.next=None
        return dummy_node.next
    