class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = [set() for i in range(len(edges))]
        usedGrp = -1
        for v1 , v2 in edges:
            v1_grp = -1
            v2_grp = -1
            for i in range(len(visited)):
                grp = visited[i]
                if v1 in grp:
                    v1_grp = i
                
            for i in range(len(visited)):
                grp = visited[i]
                if v2 in grp:
                    v2_grp = i
            
            if v1_grp == -1 and v2_grp == -1:
                v1_grp = usedGrp + 1
                v2_grp = v1_grp
                visited[v1_grp].add(v1)
                visited[v1_grp].add(v2)
                usedGrp +=1
            
            elif v1_grp == -1 :
                
                v1_grp = v2_grp
                visited[v1_grp].add(v1)
            elif v2_grp == -1 :
                
                v2_grp = v1_grp
                visited[v1_grp].add(v2)
            elif v1_grp == v2_grp:
                return [v1,v2]
            else:
                newgrp = visited[v1_grp] | visited[v2_grp]
                if v1_grp > v2_grp:
                    visited.pop(v1_grp)
                    visited.pop(v2_grp)
                else:
                    visited.pop(v2_grp)
                    visited.pop(v1_grp)
                
                visited.append(newgrp)
                usedGrp += 1
