class Solution:
    def trap(self, height: List[int]) -> int:
        preMax=[0]*len(height)
        postMax=[0]*len(height)
        maxi=height[0]
        
        for i in range(len(height)):
            preMax[i] = maxi
            maxi = max(maxi , height[i])
        maxim = height[-1]
        for j in range(len(height)-2,-1,-1):
            postMax[j]=maxim
            maxim = max(maxim,height[j])
            # print(maxim)
        # print(preMax,postMax)
        water = 0
        for i in range (len(height)):
            if min(preMax[i] , postMax[i]) - height[i] >0:
                water+=min(preMax[i] , postMax[i]) - height[i];

        return water
