class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        place_dict_zero = defaultdict(lambda:0)
        place_dict_ones = defaultdict(lambda:0)
        max_len = len(format(max(nums), 'b'))
        
        def create_bin(num):
            bin_num = format(num,'b').zfill(max_len)
            for i,c in enumerate(bin_num):
                if c == '0':
                    place_dict_zero[i] += 1
                else:
                    place_dict_ones[i] += 1
                
        
        for num in nums:
            create_bin(num)
        
       
        #print(place_dict_zero,place_dict_ones)
        res = 0
        for i in range(max_len):
            res += (place_dict_zero[i] * place_dict_ones[i])
    
        
        return res
    
        
        