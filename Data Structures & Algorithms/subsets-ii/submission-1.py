class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        def helper(idx,subs):
                if idx == len(nums):
                    res.append(subs.copy())
                    return

                subs.append(nums[idx])
                helper(idx+1,subs)
                subs.pop()

                while idx+1<len(nums) and nums[idx] == nums[idx+1]:
                    idx+=1
                helper(idx+1,subs)
                return
        
        helper(0,[])
        return res
