# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = [(root,0)]
        
        max_h = 0
        
        while q:
            max_h = max(max_h,q[-1][1] - q[0][1] + 1)
            temp = []
            for node,i in q:
                if node.left:
                    temp.append((node.left,2*i))
                    
                if node.right:
                    temp.append((node.right,2*i + 1))
            q = temp
                        
        return max_h
                    
                
                        
                    
        
        