class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int>v1(27,0);
        vector<int>v2(27,0);
        if (s.size() != t.size()){
            return false;
        }
        for (int i=0;i<s.size();i++){
            v1[tolower(s[i]-'a')]++;
            v2[tolower(t[i]-'a')]++;
        }
        // for (int i=0;i<v1.size();i++){
        //     cout<<v1[i]<< " ";
        // }cout<<endl;
        // for (int i=0;i<v1.size();i++){
        //     cout<<v2[i]<< " ";
        // }
        if (v1 == v2){
            return true;
        }
        else{
            return false;
        }
    }
};
