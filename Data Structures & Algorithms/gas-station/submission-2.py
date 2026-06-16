class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        cur = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur<0:
                cur = 0
                res = i+1
        return res