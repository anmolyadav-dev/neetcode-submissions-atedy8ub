class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n  = len(nums)
        l = 0
        ans = []
        for r in range(l+k-1,len(nums)):
            ans.append(max(nums[l:r+1]));
            l+=1
        return ans


            

