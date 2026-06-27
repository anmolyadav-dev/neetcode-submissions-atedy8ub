import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l<r:
            mid = l + (r-l)//2
            curHours = 0
            for pile in piles:
                curHours += math.ceil(pile/mid)
            if curHours <=h:
                r = mid 
            if curHours > h:
                l = mid + 1
            # if curHours == h:
            #     return mid
        return l
            
