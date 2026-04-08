class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucketsort
        freq = [[] for i in range(len(nums)+1)]
        count = {}

        for  n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)
        res =[]
        # print(freq)
        for i in range(len(freq)-1 , 0 , -1):
            # print(f"i = {i}")
            for j in freq[i]:
                
                # print(f"j = {j}")
                if k>0 :
                    res.append(j)
                    k-=1;


        return res