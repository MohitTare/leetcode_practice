class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        count = 1 + (arr[0] != arr[1])
        prev_diff = arr[1]  - arr[0]
        curr_diff = None
        max_count = count
        for i in range(1,len(arr) - 1):
            curr_diff = arr[i+1] - arr[i]
            
            if prev_diff * curr_diff < 0:
                count += 1
            else:
                count = 1 + (curr_diff != 0)
                
            prev_diff = curr_diff
            
            max_count = max(max_count,count)
        
        return max_count
                
                
                
            
            
        
        