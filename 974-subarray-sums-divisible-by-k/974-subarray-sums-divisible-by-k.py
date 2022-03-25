class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        d = {0:1}
        acc = 0
        for num in nums:
            acc = (acc + num) % k
            if acc in d:
                res += d[acc]
                d[acc] += 1
            else:
                d[acc] = 1
        return res
                
        