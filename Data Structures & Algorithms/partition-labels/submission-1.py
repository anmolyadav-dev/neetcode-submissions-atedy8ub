class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i , v in enumerate(s):
            hashmap[v]=i
        
        l = 0
        r = 0
        res = []
        while l<len(s) and r<len(s):
            r = hashmap[s[l]]
            k = l
            while k<r:
                r = max(r,hashmap[s[k]])
                k+=1
            res.append(r-l+1)
            l = r+1
        return res