class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            l = 0
            res = 0
            for r in range(len(nums)):
                k -= nums[r] % 2
                while k < 0:
                    k += nums[l] % 2
                    l+=1
                res += r - l + 1
                
            return res
        
        return atMost(k) -  atMost(k-1)
                
            
        
                    
                
            
                
        
        