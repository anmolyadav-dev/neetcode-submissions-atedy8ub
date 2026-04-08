class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,value in enumerate(nums):
            compliment = target -value;
            if compliment in hashmap:
                return [hashmap[compliment],i]
            
            hashmap[value]=i
            


        