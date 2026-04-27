from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(i,curVal):
           
            if curVal == amount:
                return 0
            if curVal > amount or i>=len(coins):
                return float('inf')
            
            took = 1 + solve(i,curVal+coins[i])

            nottook = solve(i+1,curVal)

            return min(took,nottook)
        minCoins = solve(0,0)
        return minCoins if minCoins != float('inf') else -1
