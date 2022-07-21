# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        self.res = 0
        cache = {}
        
        def dfs(node,curr_sum):
            if not node:
                return
            
            curr_sum += node.val
            
            if curr_sum == target:
                self.res += 1
            
            old_path_sum = curr_sum - target
            
            if old_path_sum in cache:
                self.res += cache[old_path_sum]
            
            if curr_sum in cache:
                cache[curr_sum] += 1
            else:
                cache[curr_sum] = 1
            
            
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            
            cache[curr_sum] -= 1
            
        dfs(root,0)
        
        return self.res
            
            
            
        
        
        
            
        