class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums)+1)]
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] : return dp[i]
            nottake  = dfs(i+1)

            take = nums[i] + dfs(i+2)
            dp[i]= max(take,nottake)
            return dp[i]
        
        return dfs(0)