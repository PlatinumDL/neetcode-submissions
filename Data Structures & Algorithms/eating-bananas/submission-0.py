
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Fastest rate will be k = largest -> finish eating in i hours
        #Sort the array
        piles.sort()
        #Set k to largest value -> h = len(piles)
        k = piles[-1]
        hours = len(piles)

        start = 1
        #Largest in array
        end = piles[-1]
        print(piles)

        while start <= end:
            middle = (start+end) // 2
            #Let k = middle, and calculate hours
            
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i/middle)
            #Decrease middle, to see if slower speed is still under hours
            if hours <= h:
                end = middle - 1
            #Increase k, as speed is too slow
            else:
                start = middle + 1
        
        return start