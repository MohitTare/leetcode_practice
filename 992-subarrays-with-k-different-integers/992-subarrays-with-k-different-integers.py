class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(k):
            count_num = defaultdict(lambda:0)
            l=0
            res = 0
            for r in range(len(nums)):
                if count_num[nums[r]] == 0:
                    k -= 1
                
                count_num[nums[r]] += 1
                
                while k < 0:
                    count_num[nums[l]] -= 1
                    if count_num[nums[l]] == 0:
                        k+=1
                    l+=1
                res += r - l + 1
            return res
        
        return atMostK(k) - atMostK(k-1)
        