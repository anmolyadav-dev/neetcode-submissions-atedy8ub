class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest = [[0 for i in range(len(text2))] for j in range(len(text1))]
        i = 0
        j = 0

        def lcs(i,j,longest):
            if i==len(text1) or j==len(text2):
                return 0
            if longest[i][j] :
                return longest[i][j]
            if text1[i]==text2[j]:
                longest[i][j]= 1 + lcs(i+1,j+1,longest)
            else:
                longest[i][j] = max(lcs(i+1,j,longest) , lcs(i,j+1,longest)) 
            
            return longest[i][j]
        

        return lcs(0,0,longest)