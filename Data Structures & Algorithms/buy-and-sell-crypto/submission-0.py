class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        highest = 0
        #Iterate through the list. Keep track of profit at every iteration
        for i in range(1,len(prices)):
            cur = prices[i]
            curProfit = cur - lowest
            if curProfit > profit:
                profit = curProfit
            if cur < lowest:
                lowest = cur
        
        return profit
            
        