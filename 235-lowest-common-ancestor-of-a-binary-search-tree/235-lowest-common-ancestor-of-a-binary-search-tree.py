# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        big = p.val if p.val >=q.val else q.val
        small = p.val if p.val < q.val else q.val
        
        
        
        
        def ch(root):
            if not root : 
                return 
            if  small <= root.val <= big :
                return root
            if root.val < small:
                return ch(root.right)
            if root.val > small:  
                return  ch(root.left) 
        
        return ch(root)