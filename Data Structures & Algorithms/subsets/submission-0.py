class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.sub(nums,0,[])
        return self.ans    
    def sub(self, nums,i , res):
        if i >= len(nums):
            self.ans.append(list(res))
            return
        # take 
        res.append(nums[i])
        self.sub(nums,i+1,res)
        res.pop()
        # not take
        self.sub(nums,i+1,res)