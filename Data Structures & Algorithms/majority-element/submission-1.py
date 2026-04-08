class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = -1
        for i in nums:
            if count == 0: res = -1;
            if res == -1 :
                res = i
                count = 1
                continue
            if i != res:
                count-=1
                
            else :
                count+=1
        return res 