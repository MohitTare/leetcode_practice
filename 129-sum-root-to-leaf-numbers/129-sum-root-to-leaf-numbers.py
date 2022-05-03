# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def dfs(node,total):
            
            if not node:
                return 
            
            total.append(str(node.val))
            if not node.left and not node.right:
                self.ans += int("".join(total))
            dfs(node.left,total)
            dfs(node.right,total)
            total.pop()
            
        
        dfs(root,[])
        return self.ans
            
            
            
            
        