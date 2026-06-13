class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1=[0 for i in range(len(nums))]
        dp2=[0 for i in range(len(nums))]
        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:len(nums)]
        if len(nums) == 1: return nums[0]
        if len(nums)==2: return max(nums[0],nums[1])
        dp1[-2]=nums1[-1]
        dp2[-2]=nums2[-1]
        for i in range(len(nums1)-2,-1,-1):
            dp1[i] = max(dp1[i+1],nums1[i]+dp1[i+2])
         
        for i in range(len(nums2)-2,-1,-1):
            dp2[i] = max(dp2[i+1],nums2[i]+dp2[i+2])
        # print(dp1,dp2)
        return max(dp1[0],dp1[1],dp2[0],dp2[1])