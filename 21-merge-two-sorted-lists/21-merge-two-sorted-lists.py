# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        node = dummyNode
        while list2 and list1 :
            if list1.val <= list2.val:
                nextt = list1.next
                node.next = list1
                node = node.next
                list1 = nextt
            else:
                nextt = list2.next
                node.next = list2
                node = node.next
                list2 = nextt
        
        
        if list1 :
            node.next = list1
        if list2:
            node.next = list2
            
        return dummyNode.next
                
        
        
        
    
            
            