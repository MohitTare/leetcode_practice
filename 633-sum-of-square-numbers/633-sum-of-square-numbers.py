class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_set  = set()
        for i in range(int(sqrt(c)) + 1):
            square_set.add(i**2)
            
        for num in square_set:
            if (c - num) in square_set:
                return True
        
        return False
        
        