class Solution:
    
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        
        return min(list(filter(isSubsequence,dictionary)) + [''],key = lambda x: (-len(x),x))
           
            
                
                    