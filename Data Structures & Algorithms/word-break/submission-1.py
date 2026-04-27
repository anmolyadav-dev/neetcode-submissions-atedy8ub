from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        class Trie:
            def __init__(self):
                self.children= {}   
                self.end = False             
            def add(self,word):
                cur = self
                for ch in word:
                    if ch not in cur.children:
                        cur.children[ch] = Trie()
                    cur = cur.children[ch]
                cur.end = True
        
            
        pref = Trie()
        for word in wordDict:
            pref.add(word)
        @lru_cache(None)
        def solve(i):
            if i == len(s):
                return True
            cur = pref
            for j in range(i,len(s)):
                if s[j] not in cur.children:
                    return False
                cur = cur.children[s[j]]
                if cur.end and solve(j+1):
                    return True
            return False
        return solve(0)
