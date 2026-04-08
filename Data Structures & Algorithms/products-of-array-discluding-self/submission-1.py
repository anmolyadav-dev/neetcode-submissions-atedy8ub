class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]
        temp=1
        for i in range(0,len(nums)-1):
            temp=temp*nums[i]
            ans.append(temp)
        temp=1
        print(ans)
        for i in range(len(nums)-2,-1,-1):
            temp*=nums[i+1]
            ans[i]*=temp
        return ans