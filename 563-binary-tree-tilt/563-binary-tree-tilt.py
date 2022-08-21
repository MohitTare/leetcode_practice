# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tilt=0
        
        def dfs(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.tilt += abs(left-right)
            
            return left+right+node.val
            
        dfs(root)
        return self.tilt
            
        