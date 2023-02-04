# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr_ptr = head
        l = 0
        while curr_ptr:
            curr_ptr = curr_ptr.next
            l+=1
        
        curr_ptr = head
        for i in range(l//2):
            curr_ptr = curr_ptr.next
            
        return curr_ptr
            
            
        