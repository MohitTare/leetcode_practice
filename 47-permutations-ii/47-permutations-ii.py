class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        len_perm = len(nums)
        visited=set()
        
        def dfs(nums,curr):
             
            if len(nums) == 0 or len(curr) == len_perm:
                if curr not in res:
                    res.append(curr[:])
            
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:],curr + [nums[i]])
                
        
        
        dfs(nums,[])
        return res
        