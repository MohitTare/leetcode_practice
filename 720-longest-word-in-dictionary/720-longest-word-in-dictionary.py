class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        word_set = set([''])
        longestWord = ''
        
        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longestWord):
                    longestWord = word               
                    
        return longestWord
            
                
            
        