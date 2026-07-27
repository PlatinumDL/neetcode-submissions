class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        if r == len(prices) -1:
            return max(profit, prices[r]-prices[l])

        while r <= len(prices) - 1:
            buyPrice = prices[l]
            sellPrice = prices[r]
            profit = max(profit, sellPrice-buyPrice)

            if buyPrice > sellPrice: #I dont want
                l = r
            else: #be greedy and find better
                r += 1
        
        return profit
            
        