class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=0
            hashmap[num]+=1
        sortByValue = dict(sorted(hashmap.items(),key = lambda x:x[1] ,reverse = True))
        print(sortByValue)
        print()
        temp =list(sortByValue.keys())
        ans = []
        for i in range(k):
            ans.append(temp[i])
        return ans