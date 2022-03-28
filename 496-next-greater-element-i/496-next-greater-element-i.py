class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        gt_dic = {}
            
        # implement a decreasing monotonic stack
        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                gt_dic[num] = stack[-1]
            stack.append(num)
            
        return [gt_dic.get(num,-1) for num in nums1]
                
            
        
        
        
        