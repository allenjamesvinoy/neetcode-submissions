class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if coins is None: 
            return 0
        if len(coins) == 0:
            return 0
        if amount == 0:
            return 1

        dp = {}

        def dfs(i, amount):
            if i >= len(coins):
                return 0
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if (i, amount) in dp:
                return dp[(i, amount)]

            res1 = dfs(i, amount - coins[i])
            res2 = dfs(i + 1, amount)
            dp[(i, amount)] = res1 + res2

            return res1 + res2

        return dfs(0, amount)
            