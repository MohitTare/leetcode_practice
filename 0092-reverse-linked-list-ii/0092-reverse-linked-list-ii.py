# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None or left == right:
            return head
        
        
        dummy = ListNode(0)
        dummy.next = head
        
        tempLeft = dummy
        curr = head
        
        for i in range(left - 1):
            tempLeft = curr
            curr = curr.next
        
        prev=None
        
        for i in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
     
        tempLeft.next.next = curr
        tempLeft.next = prev
        
        
        return dummy.next
        
        
            
        