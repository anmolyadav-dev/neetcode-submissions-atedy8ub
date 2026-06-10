class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for i in words for c in i}

        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {} # false = visited , # true = in Path , not in dict = not visited
        res = []
        def dfs(ch):
            if ch in visited :
                return not visited[ch]
            
            visited[ch] = True
            for i in adj[ch]:
                if not dfs(i):
                    return False
                
            visited[ch]=False
            res.append(ch)
            return True
        for i in adj:
            if not dfs(i):
                return ""
            
        # print(res,adj)
        return "".join(reversed(res))       
                