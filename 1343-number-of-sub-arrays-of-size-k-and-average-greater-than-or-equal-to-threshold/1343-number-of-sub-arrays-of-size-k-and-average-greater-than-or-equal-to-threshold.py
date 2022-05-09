class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i = 0
        curr_sum = 0
        
        for j in range(len(arr)):
            curr_sum += arr[j]
            #print(i,j,arr[i:j+1],curr_sum/k)
            win_len = j - i + 1
            if win_len == k:
                if curr_sum/k >= threshold:
                    res += 1
                curr_sum -= arr[i]
                i+=1
            elif win_len > k:
                curr_sum -=arr[i]
                i+=1
        return res
            
            
        