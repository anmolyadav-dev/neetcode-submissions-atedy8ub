class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for ind in range(len(nums)-2,-1,-1):
            if nums[ind]!=0: continue

            i = ind-1
            ct = 0
            bypassed = False
            while i>=0:
                ct+=1
                if nums[i] > ct:
                    bypassed= True
                else:
                    i-=1
            if bypassed == False:
                return False
            else:
                continue
        return True

