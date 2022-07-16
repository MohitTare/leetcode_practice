# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(nodel,noder):
            if not nodel and noder:
                return False
            elif not noder and nodel:
                return False
            elif not nodel and not noder:
                return True
            elif nodel.val != noder.val:
                return False
            return dfs(nodel.left,noder.right) and dfs(nodel.right,noder.left)
            
        if not root:
            return False
        
        return dfs(root.left,root.right)
            