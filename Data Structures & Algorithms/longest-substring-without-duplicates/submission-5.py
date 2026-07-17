class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        i = 0
        for r in range(len(s)):
            if s[r] in seen:
                while s[i]!= s[r]:
                    seen.remove(s[i])
                    i+=1
                else:
                    i+=1
            else:
                seen.add(s[r])
            res = max(res,r-i+1)
        
        return res