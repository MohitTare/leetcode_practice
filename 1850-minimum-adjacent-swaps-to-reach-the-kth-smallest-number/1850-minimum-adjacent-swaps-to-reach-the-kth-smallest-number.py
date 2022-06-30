class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
         
        # Swap
        
        def get_min_swaps(nums,nums0):
            count = 0
            for i in range(len(nums)):
                if nums[i] != nums0[i]:
                    k = i + 1
                    while nums0[k] != nums[i]:
                        k += 1
                    
                    while k != i:
                        nums0[k], nums0[k-1] = nums0[k-1], nums0[k]
                        count += 1
                        k-=1
            return count
        
        def getNextPerm(nums):
            i = len(nums) - 2
            while nums[i] >= nums[i+1]:
                i-=1
                
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j-=1
                
            # swap
            nums[j],nums[i] = nums[i],nums[j]
            
            nums = nums[:i+1] + sorted(nums[i+1:])
            
            return nums
        
        
        nums = [int(x) for x in num]
        nums0 = [int(x) for x in num]
        for _ in range(k):
            nums = getNextPerm(nums)
        #    print(nums)
        
        
        min_swaps = get_min_swaps(nums,nums0)
        
        return min_swaps
        
            
        