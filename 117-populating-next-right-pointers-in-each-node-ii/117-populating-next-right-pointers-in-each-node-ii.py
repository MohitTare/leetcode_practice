"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        
        queue = deque([root])
        
        while queue:
            rightNode = None
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr.next = rightNode
                rightNode = curr
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        
        return root
        