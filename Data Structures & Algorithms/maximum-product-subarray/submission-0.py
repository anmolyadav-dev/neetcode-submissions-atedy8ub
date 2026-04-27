class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = max(nums)
        for i in range(len(nums)):
            curProd = 1
            for j in range(i,len(nums)):
                curProd *= nums[j]
                if curProd > maxprod:
                    maxprod = curProd
        return maxprod

        