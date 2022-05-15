"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
            
            if len(stack) > 0:
                curr.next =  stack[-1]
                stack[-1].prev = curr
            
            curr.child = None
            
        return head
            
            
            