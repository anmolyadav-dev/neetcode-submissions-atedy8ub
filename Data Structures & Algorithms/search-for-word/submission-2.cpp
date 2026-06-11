class Solution {
public:

    bool dfs(int r,int c,int i,pair<int,int>par, string &word,vector<vector<char>>&board)
    {
        if (i==word.size())return true;
        if (r<0 || c<0 || r>=board.size() || c>=board[0].size()){
            return false;
        }
        int parent_r = par.first;
        int parent_c = par.second;

        if (word[i]!= board[r][c]) return false;

        vector<pair<int,int>>pos = {{-1,0},{1,0},{0,1},{0,-1}};
        for (auto &[dr,dc] : pos){
            int nr = r + dr;
            int nc = c + dc;
            if (nr==parent_r && nc==parent_c) continue;
            if (dfs(nr,nc,i+1,{r,c},word,board))return true;
        }
        return false;
        
    }
    bool exist(vector<vector<char>>& board, string word) {
        if (word.size() > board.size()*board[0].size())return false;
        for (int r=0;r<board.size();r++){
            for (int c=0;c<board[0].size();c++){
                if (board[r][c] == word[0]){
                    if (dfs(r,c,0,{-1,-1},word,board)) return true;
                }
            }
        }
        return false;
    }
};
