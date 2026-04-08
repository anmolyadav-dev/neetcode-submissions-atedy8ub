class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        res = 0
        hashmap = {}
        while l<n and r<n:
           
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
                
            # print(hashmap , win)
            #counting most freq character
            # mostfreq = 0
            # maxval = 0
            # for key,value in hashmap.items():
            #     if value>=maxval:
            #         mostfreq = key
            #         maxval = value
            
            while (r-l+1) - max(hashmap.values()) > k:
                hashmap[s[l]]-=1
                l+=1
                # hashmap[s[r]]-=1
            # win=r-l+1;
            # print(f"next win={win}")
            res = max(res,r-l+1)
            r+=1
            
        return res
            

            



        