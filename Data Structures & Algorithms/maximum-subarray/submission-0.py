class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        i = 0
        j = 0
        n = len(nums)
        while j<n and i<n:
            curSum = 0
            j = i
            print("i =",i)
            while j<n and curSum>=0:
                print("j = ",j)
                curSum+=nums[j]
                maxSum = max(maxSum,curSum)
                j+=1
               
            i = j
        return maxSum
            