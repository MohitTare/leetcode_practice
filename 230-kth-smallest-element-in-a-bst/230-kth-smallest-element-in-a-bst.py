# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
                
            k-=1
            if k == 0:
                return stack[-1].val
            root = stack.pop()
            root = root.right
        
            
            
        