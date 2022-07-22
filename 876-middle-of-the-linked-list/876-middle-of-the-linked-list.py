# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s= head
        i = 1
        while s.next:
            s = s.next 
            i+=1
        i = ceil(i/2)
        while i != 0:
            i-=1
            head = head.next
        return head