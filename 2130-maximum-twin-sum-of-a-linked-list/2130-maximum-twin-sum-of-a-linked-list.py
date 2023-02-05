# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        vals = []
        max_sum = -float('inf')
        
        curr_ptr = head
        while curr_ptr:
            vals.append(curr_ptr.val)
            curr_ptr = curr_ptr.next
        
        l = 0
        r = len(vals) - 1
        
        while l < r:
            max_sum = max(max_sum,vals[l] + vals[r])
            l+=1
            r-=1
        
        return max_sum
            
        