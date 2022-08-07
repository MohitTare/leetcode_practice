# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        node_child_dict ={}
        
        
        def dfs(node):
            if not node:
                return 'X'
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            temp = str(node.val) + ',' + left + ',' + right
            
            if temp in node_child_dict:
                node_child_dict[temp][0] += 1
            else:
                node_child_dict[temp] = [1,node]
           
            return temp
            
        dfs(root)
                
        #print(seen)   
        return [v[1] for k,v in node_child_dict.items() if v[0] > 1]
            
            
            
                
            
            
        
        
        
        