class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for c in s:
            if c == '[':
                stack.append(c)
            elif len(stack) > 0:
                stack.pop()
                
        return (len(stack) + 1 ) //2
        