class Solution {
public:
    void solve(vector<int>& nums,int target,int ind,vector<vector<int>>&res,vector<int>&temp){
        if (target == 0){
            res.push_back(temp);
        }
        if (ind == nums.size()){
            return;
        }
        if (target < nums[ind]){
            return;
        }
        temp.push_back(nums[ind]);
        solve(nums,target-nums[ind],ind,res,temp);
        temp.pop_back();
        solve(nums,target,ind+1,res,temp);

    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());  
        vector<vector<int>>res;
        vector<int>temp;
        solve(nums,target,0,res,temp);
        return res; 
    }
};
