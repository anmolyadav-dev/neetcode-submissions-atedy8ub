class Solution {
public:
    vector<char>res;
    bool dfs(char ch,map<char,bool> &visited,map<char,set<char>>&adj){
        if (visited.find(ch) != visited.end()){
            return !visited[ch];
        }
        visited[ch] = true;
        for (char i:adj[ch]){
            if (!dfs(i,visited,adj)){
                return false;
            }

        }
        visited[ch]=false;
        res.push_back(ch);
        return true;
    }
    string foreignDictionary(vector<string>& words) {
        map<char,set<char>>adj;
        for (int i = 0;i<words.size();i++){
            for (char j:words[i]){
                adj[j] = {};
            }
        }
        for (int i=0;i<words.size()-1;i++){
            string w1 = words[i];
            string w2 = words[i+1];
            int minlen = min(w1.size(),w2.size());

            if (w1.size()>w2.size() && w1.substr(0,minlen) == w2.substr(0,minlen)){
                return "";
            }

            for (int j = 0;j<minlen;j++){
                if (w1[j] != w2[j]){
                    adj[w1[j]].insert(w2[j]);
                    break;
                }
            }   

        }
        map<char,bool>asdf;
        
        for (auto & [key,vals]:adj){
            if (!dfs(key,asdf,adj)){
                return "";
            }
        }
        string ans = "";
        for (char c:res){
            ans = c + ans;
        }
        return ans;
    }
};
