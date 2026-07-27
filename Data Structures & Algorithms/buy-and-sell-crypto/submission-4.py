class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumPrice = float("inf")
        profit = 0

        for price in prices:
            minimumPrice = min(price,minimumPrice)
            #Calculate profit
            curProfit = price - minimumPrice
            profit = max(profit,curProfit)


        return profit
        