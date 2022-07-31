class Solution:
    def grayCode(self, n: int) -> List[int]:
        def binToGray(i):
            return i ^ (i>>1)
        
        return [binToGray(x) for x in range(2**n)]
        