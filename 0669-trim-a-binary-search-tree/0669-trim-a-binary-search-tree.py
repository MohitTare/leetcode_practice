# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        
        def dfs(node,low,high):
            if not node:
                return None
            
            node.left = dfs(node.left,low,high)
            node.right = dfs(node.right,low,high)
            
            if low <= node.val <= high:
                return node
                
            elif node.val < low:
                temp = node.right
                del node
                return temp
            else:
                temp = node.left
                del node
                return temp
            
            return node
        
        return dfs(root,low,high)
        

                
            