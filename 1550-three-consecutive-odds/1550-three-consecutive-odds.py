class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag_odd = False
        count = 0
        for num in arr:
            if num % 2 == 1:
                if flag_odd:
                    count += 1
                    if count == 3:
                        return True
                else:
                    flag_odd = True
                    count += 1
            else:
                flag_odd = False
                count = 0
        
        return False