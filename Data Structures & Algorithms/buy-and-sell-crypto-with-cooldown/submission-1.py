from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        @lru_cache(None)
        def sol(i,hold):
            # Return the total profit from state (i,hold)
            if i >= len(prices):
                return 0
            if hold == True:
                # sell 
                sell = prices[i] + sol(i+2,False)
                # not sell
                notsell = sol(i+1,hold)

                return max(sell,notsell)

            else:
                # buy 
                buy = -prices[i] + sol(i+1,True)
                notbuy =sol(i+1,hold)

                return max(buy,notbuy)
        return sol(0,0)