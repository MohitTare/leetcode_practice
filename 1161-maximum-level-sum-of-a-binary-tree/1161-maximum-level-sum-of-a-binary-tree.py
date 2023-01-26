# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        res = 1
        level = 0
        max_sum = -float('inf')
        
        while q:
            size = len(q)
            curr_sum = 0
            for _ in range(size):
                node = q.popleft()
                curr_sum += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            level += 1        
            if curr_sum > max_sum:
                res = level
                max_sum = curr_sum
        
        return res
                    
                
                
            
        