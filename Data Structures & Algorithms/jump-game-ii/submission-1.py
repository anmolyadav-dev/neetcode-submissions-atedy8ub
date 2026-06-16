class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")]*(len(nums)+1)
        dp[-1]=0
        dp[-2]=0
        n = len(nums)
        for i in range(len(nums)-2,-1,-1):

            for j in range(i,i+min(nums[i]+1,n-i)):
                dp[i]=min(dp[i],1+dp[j])
            # print(dp)
        return dp[0]