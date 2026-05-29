from collections import deque
from functools import lru_cache
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i:[] for i in range(n)}

        for v1,v2 in edges:
            hashmap[v1].append(v2)
            hashmap[v2].append(v1)
        
        # bfs
        visited = set()
        
        components = 0
        
        for i in range(n):
            if i in visited:
                continue
            components += 1
            q = deque([i])
            visited.add(i)

            while q :
                x = q.popleft()
                for nei in hashmap[x]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)  
        return components 