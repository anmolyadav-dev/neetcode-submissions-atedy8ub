class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        r = mountainArr.length()-1

        while l<r:
            mid = l + (r-l)//2
            if mountainArr.get(mid) <= mountainArr.get(mid+1):
                l = mid +1
            else:
                r = mid
        peak = l
        l = 0
        r = peak
        while l<=r:
            mid = l + (r-l)//2
            val = mountainArr.get(mid)
            if val==target:
                return mid
            elif val <target:
                l = mid+1
            else:
                r = mid-1
        l = peak
        r = mountainArr.length()-1
        while l<=r:
            mid = l + (r-l)//2
            val = mountainArr.get(mid)
            if val==target:
                return mid
            elif val < target:
                r = mid-1
            else:
                l = mid+1
        return -1
