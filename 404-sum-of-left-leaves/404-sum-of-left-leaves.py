# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.left_sum = 0
        
        def dfs(node,isLeft):
            if not node:
                return 
            if not node.left and not node.right and isLeft:
                self.left_sum += node.val
            dfs(node.left,True)
            dfs(node.right,False)
                
        dfs(root,False)
        return self.left_sum
        