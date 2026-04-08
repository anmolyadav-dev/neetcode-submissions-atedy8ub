class Solution:

    def encode(self, strs: List[str]) -> str:
        #lets start with k$ where k = len of string coming
        string = ""
        for st in strs:
            l = len(st)
            string = string + str(l) + "$" + st
        return string
    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            
            l = ""
            while i<len(s) and s[i] != "$":
                l = l+ s[i]
                i+=1
            i+=1
            c = int(l)
            lst.append(s[i:i+c])
            i+=c
        return lst