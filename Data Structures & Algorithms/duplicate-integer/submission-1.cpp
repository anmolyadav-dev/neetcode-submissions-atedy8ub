class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for (int i=0;i<nums.size();i++){
            if (i+1 < nums.size() and nums[i+1]==nums[i]){
                return true;
            }

        }
        return false;
    }
};