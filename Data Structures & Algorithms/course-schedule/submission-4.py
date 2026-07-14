class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        indegree= [0]*n
        adjlist = {i:[] for i in range(n)}
        for a,b in prereq:
            adjlist[b].append(a)
            indegree[a]+=1
        q = deque()
        visited = set()
        for i in range(n):
            if (indegree[i]==0):
                q.append(i)
                
        while q:
            x = q.popleft()
            visited.add(x)

            for i in adjlist[x]:
                if i in visited:
                    return False
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(visited) != n:
            return False
        return True