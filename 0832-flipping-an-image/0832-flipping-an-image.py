class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
            
        def flip(image1):
            l = 0
            r  = len(image1) - 1

            while l < r:
                image1[l],image1[r] = image1[r],image1[l]
                l += 1
                r -= 1
                
            for i in range(len(image1)):
                image1[i] = int(not image1[i])
            
            return image1
        
        
        for r in range(len(image)):
            image[r] = flip(image[r])
               
            
        return image
        
        