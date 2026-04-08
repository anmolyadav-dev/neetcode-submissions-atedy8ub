class Solution:
    def findMin(self, nums: List[int]) -> int:
        n  = len(nums)

        l = 0 
        r = n - 1
        mini = float("inf")
        while l<=r:
            mid = l + (r-l)//2
            if nums[(mid)] < nums[r]:
                mini = min(nums[mid],mini)
                r = mid -1
            else:
                l = mid + 1
            
        return min(mini,nums[mid])
