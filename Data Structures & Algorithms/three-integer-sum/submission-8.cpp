class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>>res;
        int i = 0;
        while(i<nums.size()){
            while (i>0 &&  i < nums.size() && nums[i]==nums[i-1]){
                i++;
            }
            if (i==nums.size())break;
            int target = -nums[i];
            int l = i+1;
            int r = nums.size()-1;
            while (l<r){
                
                if (nums[l] + nums[r]==target){
                    res.push_back({nums[i],nums[l],nums[r]});
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l-1]) l++;
                    while(l < r && nums[r] == nums[r+1]) r--;
                }
                else if (nums[l]+nums[r] > target){
                    r--;
                }else l++;
            }

            i++;
        }
        return res;
    }
};
