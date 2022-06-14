# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next : return None
        
        curr1 = head
        dummyNode = ListNode()
        dummyNode.next = head
        for i in range(n):
            curr1 = curr1.next 
        
        curr2 = dummyNode
        while curr1:
            curr1 = curr1.next
            curr2 = curr2.next
        
        
        curr2.next = curr2.next.next
        
        return dummyNode.next