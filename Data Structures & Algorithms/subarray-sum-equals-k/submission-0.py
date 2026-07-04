class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mp = defaultdict(int)
        mp[0]=1
        presum = 0
        res = 0
        for num in nums:
            presum+=num
            if  presum-k in mp:
                res+= mp[presum-k]
                
            mp[presum]+=1
        return res



















# class Solution {
# public:
#     int subarraySum(vector<int>& nums, int k) {
#         unordered_map<int,int>mp;
#         mp[0] = 1;
#         int prefixSum = 0;
#         int count =0 ;
#         for(int num:nums)
#         {
#             prefixSum += num;
#             if(mp.find(prefixSum - k) != mp.end())
#             {
#                 count+= mp[prefixSum - k];
#             }
#             mp[prefixSum]++;
#         }
#         return count;
#     }
# };