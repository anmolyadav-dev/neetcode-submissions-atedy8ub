class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maximum = 0;
        int i =0;
        int j = heights.size()-1;

        while (i<j){
            maximum = max(min(heights[i],heights[j])*(j-i),maximum);
            if (heights[i]>heights[j]){
                j--;

            }else{
                i++;
            }
        }
        return maximum;
    }
};
