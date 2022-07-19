# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res = []
        
        if not root:
            return []
        
        
        def dfs(node,curr_level):
            if not node:
                return 
            q.append((node.val,curr_level))
            #if node.left:
            #    q.append(node.left.val)
            #if node.right:
            #    q.append(node.right.val)
            dfs(node.left,curr_level + 1)
            dfs(node.right,curr_level + 1)
            
            
        dfs(root,1)
        q.sort(key=lambda x: x[1], reverse = True)
        res.append([q[0][0]])
        curr_level = q[0][1]
        for node,level in q[1:]:
            if level == curr_level:
                res[-1].append(node)
            else:
                curr_level = level
                res.append([node])
        return res
        
        