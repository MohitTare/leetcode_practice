# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(node,curr_val):
            if not node:
                return 
            
            if not node.left and not node.right:
                self.res += int(curr_val,2)
                return
            
            if node.left:
                dfs(node.left, curr_val + str(node.left.val))
            
            if node.right:
                dfs(node.right, curr_val + str(node.right.val))
           
        if not root:
            return self.res
        
        dfs(root,str(root.val))
        return self.res