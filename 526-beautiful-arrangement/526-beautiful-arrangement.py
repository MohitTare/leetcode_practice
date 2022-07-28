class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        
        def dfs(nums,i):
            if i == n+1:
                self.res += 1
                return
            
            for j in range(len(nums)):
                if not((i % nums[j]) and (nums[j] % i)):
                    dfs(nums[:j] + nums[j+1:], i+1)
                
        dfs(list(range(1,n+1)),1)
        return self.res