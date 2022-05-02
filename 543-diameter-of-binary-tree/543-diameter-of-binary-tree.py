# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterCalc(node):
            if not node:
                return 0,-1
            
            leftDiameter,leftht = diameterCalc(node.left)
            rightDiameter,rightht = diameterCalc(node.right)
            
            curr_ht = max(leftht,rightht) + 1
            
            return max(leftDiameter,rightDiameter,leftht+rightht+2), curr_ht
        
        return diameterCalc(root)[0]
            