class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        res = s[0]
        for center in range(len(s)):
            i = center - 1
            j = center + 1
            curLen = 1
            while i>=0 and j<len(s) and s[i]==s[j]:
                if s[i]==s[j]:
                    curLen+=2
                    if curLen>maxLen:
                        res = s[i:j+1]
                        maxLen = curLen
                    i-=1
                    j+=1

        for center in range(len(s)-1):
            if s[center] != s[center+1]:
                continue
            if 2>maxLen:
                maxLen=2
                res = s[center]+s[center]
            i = center - 1
            j = center + 2
            curLen = 2
            while i>=0 and j<len(s) and s[i]==s[j]:
                curLen+=2
                if curLen>maxLen:
                    res = s[i:j+1]
                    print(i,j)
                    maxLen = curLen
                i-=1
                j+=1
        
        return res

        
