class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        # print(l,r)
        while l <= r :
            center = l + (r - l )//2
            print(l,r,center)
            if nums[center] == target: return center

            if nums[center] > target:
                r = center-1
            else :
                l = center+1
        return -1
        