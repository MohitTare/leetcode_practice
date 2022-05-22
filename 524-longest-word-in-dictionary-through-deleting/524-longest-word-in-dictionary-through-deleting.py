class Solution:
    
    
    
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longestWord = ''
        searchSet = defaultdict(list)
        for i,c in enumerate(s):
            searchSet[c].append(i)
            
        dictionary.sort()
        
        def search(word,curr = -1):
            for c in word:
                if c not in searchSet:
                    return False
                vals = [val for val in searchSet[c] if val > curr]
                if len(vals) == 0:
                    return False
                curr = min(vals)
            return True
                
        
        for word in dictionary:
            if search(word):
                if len(word) > len(longestWord):
                    longestWord = word
        
        return longestWord
           
            
                
                    