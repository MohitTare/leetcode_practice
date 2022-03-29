class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        count_s = Counter(s)
        stack = []
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                while stack and ord(stack[-1]) > ord(s[i]) and count_s[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
            count_s[s[i]] -= 1
            
        return ''.join(stack)
            
            
        
            
                
                
                
            
        