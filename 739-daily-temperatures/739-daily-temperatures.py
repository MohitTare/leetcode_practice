class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)
        
        for i in range(len(temp)-1,-1,-1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            else:
                res[i] = 0
            
            stack.append(i)
        
        return res
                
        