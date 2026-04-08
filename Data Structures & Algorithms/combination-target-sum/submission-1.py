class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        dp = [[0] *(target+1)]*(len(nums)+1)
        self.bt(nums,0,target,[],ans,dp)
        return ans
    
    def bt(self, nums,i  ,target ,lst ,ans,dp ):
        if dp[i][target]:
            return
        if target==0 and lst not in ans:
            ans.append(list(lst))
        if i>= len(nums):
            return
        if target < 0 :
            return 

        # not take
        dp[i+1][target] =  self.bt(nums,i+1,target,lst,ans,dp)    

        # take
        target = target - nums[i]
        lst.append(nums[i])
        dp[i][target] =  self.bt(nums,i,target,lst,ans,dp)
        lst.pop()
        target = target + nums[i]
