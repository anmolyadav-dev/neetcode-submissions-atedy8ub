class Solution {
public:
    bool isValid(string s) {
        stack<int>st;
        map<char,char>mp = {
            {'(',')'},
            {'[',']'},
            {'{','}'}
        };
        for (char i: s){
            if (mp.find(i)!=mp.end()){
                st.push(i);
            }
            else{
                if (st.empty())return false;
                char x = st.top();
                char opp = mp[x];
                // cout<<x<<opp<<endl;
                if (opp != i){
                    // cout<<"word"<<endl;
                    return false;
                }
                st.pop();
            }
        }
        if(st.empty()){
            return true;
        }
        return false;
    }
};
