class Solution:
    def minInsertions(self, s: str) -> int:
        
        s += "$"  # appending dummy character at the end, to make things simpler
        left_braces, count, i = 0, 0, 0
        while( i < len(s)-1 ):
            if s[i] == "(":
                left_braces, i = left_braces + 1, i + 1
            elif s[i] == ")" and s[i+1] == ")":
                if left_braces:
                    left_braces -= 1
                else:
                    count += 1                  # one open brace required
                i += 2
            elif s[i] == ")" and s[i+1] != ")":
                if left_braces:
                    count += 1                  # one close brace required
                    left_braces -= 1
                else:
                    count += 2                  # one open and one close brace required
                i += 1
        return count + (left_braces * 2)        # close braces required at the end for all the remaining left braces

        
        
                
            
        
        
        
        
        