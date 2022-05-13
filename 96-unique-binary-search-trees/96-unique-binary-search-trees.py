class Solution:
    def numTrees(self, n: int) -> int:
        # Basic idea is recursion suppose we consider 2 as a root node its total number can be calculated as numTrees(1)[for root 1 on left] * numTrees(1)[ for root 3 on right]
        #basically for each number of nodes on left and right its a the prdocut here in this case 1 * 1  = 1
        # for numTrees(1) =  numTrees(0) * numTrees(2)
        
        
        
        numTrees = [0] * (n + 1)
        
        
        # empty tree and tree with just a single node
        numTrees[0] = numTrees[1] = 1
        
        
        for nodes in range(2,n+1):
            total = 0
            for root in range(1,nodes+1):
                left = root - 1
                right = nodes - root
                total += numTrees[left] * numTrees[right]
                
            numTrees[nodes] = total
            
        return numTrees[n]
        