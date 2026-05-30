from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        coins = sorted(coins)
        @lru_cache(None)
        def dfs(i:int, amountLeft:int):
            nonlocal res
            if amountLeft == 0:
                return 1
            if i >= len(coins) or amountLeft < 0 or coins[i] > amountLeft:
                return 0
            
            # take the coin
            x = dfs(i,amountLeft - coins[i])

            #not take the coini
            y = dfs(i+1,amountLeft)

            return x + y
        return dfs(0,amount)