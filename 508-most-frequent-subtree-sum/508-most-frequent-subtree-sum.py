# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        subtree_dict = defaultdict(lambda :0)
        
        def dfs(node):
            #print(node.val)
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            
            total_sum = leftSum + rightSum + node.val
            
            subtree_dict[total_sum] += 1
            return total_sum
        
        
        dfs(root)
        max_freq = max(subtree_dict.values())
        return [k for k,v in subtree_dict.items() if v == max_freq]
        
        
        
        
            
            
            
        
        
        
        
        
        