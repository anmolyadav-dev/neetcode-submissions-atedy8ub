class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perm = [[]]

        for num in nums:
            nextPerm = []
            print("perm = ",perm,len(perm))
            for p in perm:
                for i in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(i,num)
                    nextPerm.append(pcopy)
                    print(pcopy,nextPerm)
                print("middle loop")
            perm = nextPerm
        return perm
