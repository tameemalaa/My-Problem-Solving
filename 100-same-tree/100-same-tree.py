# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return check(p,q)        
def check(node1,node2):
    
        
    if node1 is None and node2 is None :
        return True
    if (node1 == None) ^ (node2 == None) :
        return False 
    if node1 is not None  and node1 is not None :
        return check(node1.right, node2.right) and check(node1.left, node2.left) and (node1.val == node2.val)
    return False