class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        int r = 0;
        int res = k;
        map<char,int>mp;
        multiset<int>multi;
        while (r<s.size()){
            mp[s[r]]++;
            multi.insert(mp[s[r]]);
            if (r-l+1 - *multi.rbegin() > k){
                multi.erase(mp[s[l]]);
                mp[s[l]]--;
                multi.insert(mp[s[l]]);
                l++;
            }

            res = max(res,r-l+1);
            r++;

        }
        return res;
    }
};
