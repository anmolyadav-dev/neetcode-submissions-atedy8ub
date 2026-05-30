from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # building an adjacancy list
        adj = {}
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in adj:
                    adj[pattern]=[]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        print(adj)
        while q:
            for i in range(len(q)):
                wrd = q.popleft()
                if wrd == endWord:
                    return res
                for j in range(len(wrd)):
                    pattern = wrd[:j] + "*" + wrd[j+1:]

                    for nei in adj[pattern]:
                        
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res+=1
        return 0

