# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = defaultdict(list)
        def lot(node,level):
            if not node : return
            lot(node.left,level+1)
            lot(node.right,level+1)
            lookup[level].append(node.val)
            return
        lot(root,0)
        return [lookup[i] for i in range(len(lookup.keys()))]
    