# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first = []
        second = []
        
        def dfs(node,curr):
            if not node:
                return
            if not node.left and not node.right:
                curr.append(node.val)
                
            dfs(node.left,curr)
            dfs(node.right,curr)
            
        dfs(root1,first)
        dfs(root2,second)
        
        return first == second
            
        