class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preMult=[1]
        postMult=[1]
        for i in range(1,len(nums)):
            preMult.append(preMult[-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            postMult.insert(0,postMult[0]*nums[i+1])
        
        ans = []
        for i in range(len(nums)):
            ans.append(preMult[i]*postMult[i])
        return ans 
        