from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums)+1)]
        hashmap = Counter(nums)
        for i,val in hashmap.items():
            count[val].append(i)
        res=[]
        for i in range(len(nums),-1,-1):
            if count[i]:
                for j in count[i]:
                    res.append(j)
                    k-=1
                    if k<=0:
                        return res
            if k<=0:
                return res

            
        