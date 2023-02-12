# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        total_len = 0
        curr = head
        while curr:
            total_len += 1
            curr = curr.next
        
        curr_l =  head
        curr_r = head
        
        for i in range(k - 1):
            curr_l = curr_l.next
        
        
        for i in range(total_len - k):
            curr_r = curr_r.next
            
            
        #print(curr_l.val,curr_r.val)
        
        curr_l.val,curr_r.val =  curr_r.val,curr_l.val
        
        
        return head
            
        
        
        
        
            
        