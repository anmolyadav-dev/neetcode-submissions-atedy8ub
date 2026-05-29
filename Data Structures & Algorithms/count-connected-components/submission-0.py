class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjacency list
        hashmap = {i:[] for i in range(n)}

        for v1,v2 in edges:
            hashmap[v1].append(v2)
            hashmap[v2].append(v1)

        visited = set()
        def dfs(v):
            if v in visited:
                return False
            visited.add(v)
            for child in  hashmap[v]:
                if child not in visited:
                    dfs(child)  
            
            return True
        ans = 0
        for i in range(n):
            if dfs(i):
                ans+=1
        return ans