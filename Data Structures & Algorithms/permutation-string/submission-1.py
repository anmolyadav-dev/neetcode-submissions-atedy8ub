class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)-1
        freq1 = {}
        freq2 = {}
        if len(s2) < len(s1) : return False
        for i in s1:
            freq1[i] = 1 + freq1.get(i,0)
        for i in range(0,len(s1)):
            freq2[s2[i]]= 1 + freq2.get(s2[i],0)

        while l<len(s2) and r<len(s2):

            if freq1 == freq2 :
                return True
            else:

                if r != len(s2)-1:
                    freq2[s2[l]]-=1
                    if freq2[s2[l]] == 0:
                        freq2.pop(s2[l])
                    freq2[s2[r+1]]=1+freq2.get(s2[r+1],0)
                l+=1 
                r+=1
            print(freq1 , freq2)


            
        return False
        