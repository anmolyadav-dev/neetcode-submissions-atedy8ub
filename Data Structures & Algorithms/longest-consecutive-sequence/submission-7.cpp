class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 1;
        if (nums.size()==0)return 0;
        unordered_set<int>st;
        for (int i=0;i<nums.size();i++){
            st.insert(nums[i]);
        }
        for (int i=0;i<nums.size();i++){
            if (st.count(nums[i]-1))continue;
            if (!st.count(nums[i]+1))continue;
            int ct = 1;
            int temp = nums[i];
            while (st.count(temp+1)){
                temp++;
                ct++;
                res = max(res,ct);
            }
        }
        return res;
    }
};
