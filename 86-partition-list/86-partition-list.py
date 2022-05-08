# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = start = None
        stack = []
        
        if head is None:
            return head
                
        while head:
            if head.val < x and start is None:
                res = head
                start = head
                head = head.next
            elif head.val < x and start is not None:
                start.next = head
                head = head.next
                start = start.next    
            elif head.val >= x:
                stack.append(head)
                head = head.next
            
        
        if start is None:
            return stack[0]
        
        
        for i in range(len(stack)):                
            start.next = stack[i]
            stack[i].next = None
            start = start.next
            
        return res
        
        
        
                
            
        
        