# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res = []
        
        def dfs(node,curr):
            #print(node.val,curr) if node else print("None",curr)
            if not node:
                return
            
            
            curr.append(node.val)
            if sum(curr) ==  target and not node.left and not node.right:
                #print(node)
                res.append(curr[:])
            dfs(node.left,curr)
            dfs(node.right,curr)
            curr.pop()
        
        dfs(root,[])
        return  res