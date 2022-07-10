# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        l = 0
        while curr:
            stack.append(curr)
            curr = curr.next
            l+=1
            
        
        curr = head
        #print(l)
        for i in range(l//2):
            temp = curr.next
            last = stack.pop()
            #print(f"last {last.val}")
            curr.next = last
            last.next = temp
            curr = curr.next.next
        
        curr.next=None
        return head
        