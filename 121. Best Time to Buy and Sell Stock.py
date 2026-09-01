# Accepted
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0

        for num in prices[1:]:
            if(buyPrice > num):
                buyPrice = num

            profit = max(profit, num - buyPrice)

        return profit