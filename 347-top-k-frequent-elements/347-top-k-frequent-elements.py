class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)
        
        for key in counter:
            heapq.heappush(heap,(counter[key],key))
            
        return [num for _,num in heapq.nlargest(k,heap)]
        