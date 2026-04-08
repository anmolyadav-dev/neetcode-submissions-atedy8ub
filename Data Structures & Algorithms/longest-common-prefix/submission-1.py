class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        smallest_str = min(strs,key=len)
        for i in range(len(smallest_str)):
            temp = smallest_str[i]
            for j in range(len(strs)):
                if strs[j][i] != temp:
                    return res
            res+= temp;
        return res