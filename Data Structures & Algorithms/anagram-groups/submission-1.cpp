class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>mp;
        for(string str:strs){
            string str_copy = str;
            sort(str_copy.begin(),str_copy.end());
            mp[str_copy].push_back(str);
        }
        vector<vector<string>>res(mp.size());
        int ct = 0;
        for (auto &[a,vec]:mp){
            for (string st:vec){
                res[ct].push_back(st);
            }
            ct++;
        }
        return res;
    }
};
