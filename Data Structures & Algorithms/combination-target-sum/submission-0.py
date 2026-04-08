class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        self.bt(nums,0,target,[],ans)
        return ans
    
    def bt(self, nums,i  ,target ,lst ,ans ):
        if target==0 and lst not in ans:
            ans.append(list(lst))
        if i>= len(nums):
            return
        if target < 0 :
            return 

        # not take
        self.bt(nums,i+1,target,lst,ans)    

        # take
        target = target - nums[i]
        lst.append(nums[i])
        self.bt(nums,i,target,lst,ans)
        lst.pop()
        target = target + nums[i]
