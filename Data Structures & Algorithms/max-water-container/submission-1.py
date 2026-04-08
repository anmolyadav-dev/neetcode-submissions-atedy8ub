class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        maxHeight=0;
       
        maxArea=0
        while i<j:
            
            print(f"i= {i} : h[i]= {heights[i]} and j={j} : h[j]= {heights[j]}")
            currHeight = min(heights[i],heights[j])
            currWidth = j-i
            currArea = currHeight * currWidth;
            if (currArea > maxArea):
                maxHeight = currHeight;
                maxWidth = currWidth
                maxArea = currHeight * currWidth;

            print(f"area = {currArea} ==> maxarea = {maxArea}")
            if (heights[i]<heights[j]):
                i+=1;
            else:
                j-=1;
        return maxArea;
