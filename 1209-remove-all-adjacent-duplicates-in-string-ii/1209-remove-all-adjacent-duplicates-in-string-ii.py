class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['$',0]]
        
        for c in range(len(s)):
            if stack[-1][0] == s[c]:
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
            else:        
                stack.append([s[c],1])
        
        return ''.join([s*c for s,c in stack])
            
                
                    
        