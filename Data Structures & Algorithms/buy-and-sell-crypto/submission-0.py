class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        postMax = 0

        for i in range(len(prices)-2,-1,-1):
            postMax = max(prices[i+1],postMax)
            profit = postMax - prices[i] 
            if profit > 0:
                maxProfit = max(profit,maxProfit)
            # print(postMax,profit)
        return maxProfit