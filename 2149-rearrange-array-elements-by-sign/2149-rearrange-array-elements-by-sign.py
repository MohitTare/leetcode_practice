class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        num_pos = [x for x in nums if x >= 0]
        num_neg = [x for x in nums if x < 0]
        
        res  = []
        
        for i in range(len(nums)//2):
            res.append(num_pos[i])
            res.append(num_neg[i])
            
            
        return res
            
            
        