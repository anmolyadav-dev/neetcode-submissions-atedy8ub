class Solution {
public:
    unordered_set<int>visited;
    void dfs(int i,map<int,vector<int>> &adj){
        visited.insert(i);
        for (int j:adj[i]){
            if (!visited.count(j)){
                dfs(j,adj);
            }
        } 
    }
    bool validTree(int n, vector<vector<int>>& edges) {
        // find if its connected then edges = n-1
        map<int,vector<int>>adj;
        for (auto& edge : edges) {
            int a = edge[0];
            int b = edge[1];

            adj[a].push_back(b);
            adj[b].push_back(a);
        }
            
            
            dfs(0,adj);
        if( visited.size() == n and edges.size()==n-1){
            return true;
        }
        else{
            return false;
        }
    }
};
