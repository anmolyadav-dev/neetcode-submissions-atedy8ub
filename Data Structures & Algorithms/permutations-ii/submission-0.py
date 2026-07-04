class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = collections.Counter(nums)

        def solve():
            nonlocal count
            if len(perm) == len(nums):
                res.append(perm[:])
                return 
            
            for i in count:
                if count[i]:
                    perm.append(i)
                    count[i]-=1
                    solve()
                    count[i]+=1
                    perm.pop()
        solve()
        return res