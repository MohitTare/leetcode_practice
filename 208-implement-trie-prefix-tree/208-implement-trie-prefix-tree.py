class TrieNode:
    def __init__(self):
        self.child = {}
        self.isLeaf = False

    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.isLeaf = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            curr = curr.child.get(c,None)
            if curr is None:
                return False
        return curr.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            curr = curr.child.get(c,None)
            if curr is None:
                return False
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)