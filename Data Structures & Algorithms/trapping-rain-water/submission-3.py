class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        i = 0
        j = n-1
        
        water = 0
        while i<j:
            while i<j and (height[i]==0):
                i+=1
            while i<j and height[j]==0:
                j-=1;
            mini = min(height[i],height[j])
            for x in range(n):
                # print(mini)
                if x>i and x<j and height[x] < mini:
                    water += mini - height[x]
                if height[x]>=mini:
                    height[x] -= mini;
                else: height[x] = 0
                # print(x,height,water)
            
            # print(f"i = {i} and j = {j}")
        
        return water;
