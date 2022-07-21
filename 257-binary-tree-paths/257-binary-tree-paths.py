# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        
        def dfs(node,curr):
            
            if not node:
                return
            
            if not node.left and not node.right:
                s = "->".join([str(x) for x in curr + [node.val]])
                res.append(s)
                
            #if node.left:
            dfs(node.left,curr + [node.val])
            #if node.right:
            dfs(node.right,curr + [node.val])
            
            
        if not root:
            return [""]
        
        dfs(root,[])
        
        return res
        
        
        