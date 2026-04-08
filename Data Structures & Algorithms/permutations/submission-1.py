class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res =[]

        def helper(idxCompleted,perm):
            if len(idxCompleted) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if i in idxCompleted:
                    continue
                idxCompleted.add(i)
                perm.append(nums[i])
                helper(idxCompleted,perm)
                idxCompleted.remove(i)
                perm.pop()


        helper(set(),[])
        return res