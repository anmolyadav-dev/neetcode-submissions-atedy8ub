class Solution {
public:
    string minWindow(string s, string t) {
        if (t.size()>s.size()) return "";
        unordered_set<char>matched;
        unordered_map<char,int>freqT;
        unordered_map<char,int>freqS;
        int l = 0;
        int r = 0;
        for (char i:t){
            freqT[i]++;
        }
        // built freq map of T
        // finding first accurance of element of T in S
        for (int i=0;i<s.size();i++){
            if (freqT.find(s[i]) != freqT.end()){
                // freqS[s[i]]++;
                // if (freqS[s[i]] >= freqT[s[i]]){
                //     matched.insert(s[i]);
                // }
                l = i;
                break;
            }
        }

        int minWindow = s.size();
        string res = "";
        r = l;
        while (r<s.size()){
            
            freqS[s[r]]++;
            if (freqT.find(s[r]) != freqT.end()&& freqS[s[r]] == freqT[s[r]]){
                matched.insert(s[r]);
                

                while (matched.size() == freqT.size()){
                    if (r-l+1 <= minWindow){
                        minWindow = r-l+1;
                        res = s.substr(l,r-l+1);
                    }
                    freqS[s[l]]--;
                    if (freqT.find(s[l]) != freqT.end() && freqS[s[l]] < freqT[s[l]]){
                        matched.erase(s[l]);
                    }
                    l++;
                }
            }
            r++;
            

        }
        return res;

    }
};
