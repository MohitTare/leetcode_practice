class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = deque(sentence1.split())
        words2 = deque(sentence2.split())
        
        if len(words1) < len(words2):
            words2,words1 = words1,words2
            
        
        while words2:
            if words1[0] == words2[0]:
                words1.popleft()
                words2.popleft()
            elif words1[-1] == words2[-1]:
                words1.pop()
                words2.pop()
            else:
                return False
            
        return True
        