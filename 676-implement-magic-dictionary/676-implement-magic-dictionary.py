class TrieNode:
    def __init__(self):
        self.child  = {}
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        curr  = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.isWord = True
        
    def searchfuzzy(self,node,word,count):
        # early terminate
        if count < 0:
            return False

        if not word:
            return True if count == 0 and node.isWord else False
        
        for c, nxt in node.child.items():
            if word[0] == c:
                if self.searchfuzzy(nxt, word[1:], count):
                    return True
            else:
                if self.searchfuzzy(nxt, word[1:], count-1):
                    return True
        
        return False

                
        
class MagicDictionary:

    def __init__(self):
        self.dict = Trie()
        
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict.insert(word)
        
    def search(self, searchWord: str) -> bool:
        return self.dict.searchfuzzy(self.dict.root,searchWord,1)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)