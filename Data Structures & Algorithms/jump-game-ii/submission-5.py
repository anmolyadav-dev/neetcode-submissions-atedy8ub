class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        maximum = nums[0]
        nextWindow = nums[0]
        
        if len(nums)==1:return 0
        for i in range(len(nums)):
            if nextWindow>=len(nums)-1:
                res+=1
                return res
            if i==nextWindow:
                res+=1
                maximum = max(maximum,i+nums[i])
                nextWindow = maximum
                
            maximum = max(maximum,i+nums[i])
            print()
        return res
