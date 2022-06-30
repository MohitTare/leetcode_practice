class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_l = []
        max_r = []
        max_h = 0
        
        
        for i in range(len(heights)):
            if heights[i] > max_h:
                max_l.append(max_h)
                max_h = heights[i]
            else:
                max_l.append(max_h)
        
        max_h = 0
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_h:
                max_r.append(max_h)
                max_h = heights[i]
            else:
                max_r.append(max_h)
        
        max_r = max_r[::-1]
        
        res = 0
        for i in range(len(heights)):
            if min(max_l[i],max_r[i]) - heights[i] > 0:
                res += min(max_l[i],max_r[i]) - heights[i]
                
        
        return res
        