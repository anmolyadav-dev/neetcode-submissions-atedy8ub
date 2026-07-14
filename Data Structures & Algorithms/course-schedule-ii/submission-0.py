class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        indegree= [0]*n
        adjlist = {i:[] for i in range(n)}
        for a,b in prereq:
            adjlist[b].append(a)
            indegree[a]+=1
        q = deque()
        for i in range(n):
            if (indegree[i]==0):
                q.append(i)
        res = []
        # print(indegree)
        while q:
            x = q.popleft()
            res.append(x)
            # print(x)
            for i in adjlist[x]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(res)!= n:
            return []
        return res
