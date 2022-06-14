# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root)
        
def dfs(root):
    if not(root):
        return 0
    max_depth = 0
    if root.left == None and root.right == None :
        return 1
    if root.left :
        max_depth = dfs(root.left)+1
    if root.right :
        max_depth = max(max_depth,dfs(root.right)+1)
    return max_depth
