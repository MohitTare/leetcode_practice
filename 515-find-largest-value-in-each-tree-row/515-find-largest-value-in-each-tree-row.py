# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q  = deque([root])
        res = []
        while q:
            max_num = None
            for _ in range(len(q)):
                curr = q.popleft()
                if max_num is None:
                    max_num = curr.val
                else:
                    max_num = max(max_num,curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
            res.append(max_num)
            
        return res
        
        
        