class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for c in s:
            if c == '#' :
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(c)
                
        for c in t:
            if c == '#' :
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(c)
                
        
        if stack_s == stack_t:
            return True
        else:
            return False
                
        
            