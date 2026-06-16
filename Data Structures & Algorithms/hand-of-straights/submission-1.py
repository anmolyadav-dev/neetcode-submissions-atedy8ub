class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        n = len(hand)
        if n%gs !=0:
            return False
        hand.sort()
        hashmap = {}
        for i in hand:
            hashmap[i] = 1+hashmap.get(i,0)
        
        temp = 1
        numberOfGroups = n//gs
        
        hashmap = dict(sorted(hashmap.items()))
        while temp<=numberOfGroups:
            ct=0
            el = -1
            for key,val in hashmap.items():
                if val>0:
                    el = key
                    break
            while ct<gs:
                if el == -1:
                    return False
                if el not in hashmap:
                    return False
                ct+=1
                hashmap[el]-=1
                if hashmap[el]==0:
                    del hashmap[el]
                el+=1
            temp+=1
        return True
