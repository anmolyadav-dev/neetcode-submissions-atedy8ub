class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l,r=0,1
        if len(nums)==1 : return 1
        if len(nums)==0: return 0
        count=1
        maxCount=1
        sortedNums=sorted(list(set(nums)))
        print(sortedNums)
        while r< len(sortedNums):
            if (sortedNums[r]-sortedNums[l] == 1):
                count+=1
            else: 
                count=1
            maxCount=max(maxCount,count)  
            l+=1
            r+=1   
                
                
        return maxCount
                