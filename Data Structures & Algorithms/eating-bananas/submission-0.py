class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l =1
        r = max(piles)

        
        while l<=r:
            mid = l+ (r - l)//2
            currH = 0
            for i in piles:
                currH+= (i + mid-1)//mid # ceil division
            print(mid,currH)

            if currH <= h:
                r = mid-1
            else:
                l = mid + 1
        print (l,r,mid)
        return l
        