# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        
        count = [0]
        cache = {0:1}
        
        def dfs(node,target,currSum,cache):
            if not node:
                return
            
            
            currSum += node.val
            
            oldPathSum = currSum - target
            
            count[0] += cache.get(oldPathSum,0)
            
            cache[currSum] =  cache.get(currSum,0) + 1
            
            
            dfs(node.left,target,currSum,cache)
            dfs(node.right,target,currSum,cache)
            
            cache[currSum] -= 1
            
            
        dfs(root,target,0,cache)
        return count[0]
            
            
        