class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        print(nums)
        for c in range(len(nums)-2):
            l = c+1
            r = len(nums)-1
            while l < r:
                # print(c,l,r)
                target = -1 * nums[c]
                if nums[l] + nums[r]  == target:
                    x = (nums[c],nums[l],nums[r])
                    # print(x)
                    if x not in res:
                        res.add(x)
                    l+=1
                elif nums[r] + nums[l] < target:
                    l+=1
                else:
                    r-=1
        return list(res)