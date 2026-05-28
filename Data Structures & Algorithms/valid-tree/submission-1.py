class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for n1,n2 in edges:
            if n1 not in graph:
                graph[n1]=[]
            if n2 not in graph :
                graph[n2] = []
            
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        print(graph)
        total = 0
        def dfs(node,par):
            nonlocal total
            total+=1
            if node in visited:
                return False
            visited.add(node)
            for n in graph[node]:
                if n == par:
                    continue
                dfs(n,node)
            visited.remove(node)
            
            return True
        
        return dfs(0,-1) and total == n