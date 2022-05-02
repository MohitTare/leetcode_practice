# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # Basic idea is to calculate max_h for each sub-parent 
        max_h = [0]
        
        def traverse(node,parent):
            if not node:
                return 0
            
            left = traverse(node.left,node.val)
            right = traverse(node.right,node.val)
            
            max_h[0] = max(max_h[0],left+ right)
            
            return 1 + max(left,right) if node.val == parent else 0 # pass max of left or right sub tree max_path else 0 if they are not equal
        
        traverse(root,None)
        return max_h[0]
        