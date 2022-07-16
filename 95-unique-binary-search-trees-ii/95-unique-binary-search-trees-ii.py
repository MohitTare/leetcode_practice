# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(left,right):
            if left > right : return [None]
            
            all_trees = []
            
            for currRoot in range(left,right + 1):
                allLeftTrees = dfs(left, currRoot - 1)
                allRightTrees = dfs(currRoot + 1, right)
                
                
                for leftTree in allLeftTrees:
                    for rightTree in allRightTrees:
                        currTree = TreeNode(currRoot)
                        currTree.left = leftTree
                        currTree.right = rightTree
                        all_trees.append(currTree)
                
            return all_trees
        
        
        return dfs(1,n)
                
                
                
                
            
        
        
        
        
        