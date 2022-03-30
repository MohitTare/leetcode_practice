class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        gt = defaultdict(lambda:-1)
        
        nums.extend(nums[:])
        
        for i,num in enumerate(nums[::-1]):
            while stack and num >= stack[-1]:
                stack.pop()
            if stack:
                gt[(len(nums) - 1) - i] = stack[-1]
            stack.append(num)
            
        return [gt[i] for i in range(len(nums) // 2)]
        