class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')   
            if amount in memo:
                return memo[amount]
            
            res = min(dfs(amount - c) + 1 for c in coins)
            memo[amount] = res
            return res
        
        result = dfs(amount)
        return result if result != float('inf') else -1