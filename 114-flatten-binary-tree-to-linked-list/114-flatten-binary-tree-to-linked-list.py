# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        
        stack = [root]
        
          
        while stack:
            curr = stack.pop()
            
            if curr.right:
                stack.append(curr.right)
                
            if curr.left:
                stack.append(curr.left)
            
            if len(stack) > 0:
                curr.right = stack[-1]
            
            curr.left = None
            
        
        return root
         
            
                
                
            
            
            
        
            
        