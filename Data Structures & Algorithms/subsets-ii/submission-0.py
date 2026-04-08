class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def helper(idx,subs):
            if idx == len(nums):
                if  sorted(subs) in res:
                    return
                res.append(sorted(subs.copy()))
                return
            
            subs.append(nums[idx])
            helper(idx+1,subs)
            subs.pop()

            helper(idx+1,subs)
            return
        
        helper(0,[])
        return res
