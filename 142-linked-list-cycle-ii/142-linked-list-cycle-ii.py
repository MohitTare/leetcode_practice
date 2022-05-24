# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        
        curr = head
        while(curr not in visited and curr is not None):
            visited.add(curr)
            curr = curr.next
            
        return curr if curr is not None else None
            
        