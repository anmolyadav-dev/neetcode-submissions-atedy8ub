class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        mini = float('inf')
        si=0

        while l<=r:
            mid = l + (r - l)//2
            if mini > nums[mid] :
                si = mid
                mini = nums[mid]
            
            if nums[mid] < nums[r]:
                r = mid -1
            else:
                l = mid + 1

        # print(mini,si)    
        
        
    

        if target > nums[-1]:
            l = 0 
            r = si -1
        else:
            l = si
            r = len(nums)-1

        while l<=r:
            mid = l + (r-l)//2

            if nums[mid] == target: return mid
            
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return -1
        