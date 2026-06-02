class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i,v in enumerate(s):
            if v not in hashmap:
                hashmap[v]=[i,i]
            elif v in hashmap:
                hashmap[v] = [hashmap[v][0],i]
        
        l = 0
        k = l
        print(hashmap)
        res = []
        while k<len(s):
            window = hashmap[s[l]]

            r = window[1]
            k = l 

            while k<=r:
                if hashmap[s[k]][1] > r:
                    r = hashmap[s[k]][1]
                k+=1
            res.append(r-l+1)
            l = r+1
        return res



            
