class Solution {
public:
    bool dfs(int i,unordered_map<int,vector<int>>&adj,unordered_set<int>&visited,unordered_set<int>&cycle){
        if (cycle.count(i))return false;
        if (visited.count(i))return true;
        visited.insert(i);
        cycle.insert(i);
        for (int neighbor:adj[i]){

            if(!dfs(neighbor,adj,visited,cycle))return false;
        }
        cycle.erase(i);
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // adj matix : node -> preReq
        unordered_map<int,vector<int>>adj;
        for (const auto &p : prerequisites) {
    adj[p[0]].push_back(p[1]);
}
        unordered_set<int>visited;
        unordered_set<int>cycle;
        for (int i=0;i<numCourses;i++){
            if(!dfs(i,adj,visited,cycle))return false;
        }
        if (visited.size()!= numCourses)return false;
        return true;
    }
};
