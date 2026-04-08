class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for key, cou in count.items():
            freq[cou].append(key)
        
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                return freq[i][0]
            
         
        