class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 0:
            return 0

        max_price = prices[-1]

        res = 0

        for i in range(l-2, -1, -1):
            if prices[i] < max_price:
                res = max(res, max_price-prices[i])
            else:
                max_price = prices[i]

        return res