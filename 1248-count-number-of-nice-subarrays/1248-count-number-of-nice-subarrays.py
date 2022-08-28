class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dict_count = {0:1}
        count = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1
            
            if count - k in dict_count:
                res += dict_count[count - k]
                
            dict_count[count] = dict_count.get(count,0) + 1
            
        return res
        
                    
                
            
                
        
        