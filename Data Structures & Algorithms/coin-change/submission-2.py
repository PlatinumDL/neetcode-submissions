class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #DP Array
        dp = [float('inf')] * (amount + 1)

        if amount == 0:
            return 0
        
        #Initialize base cases
        for coin in coins: #Number of coins for the coin value itself is just 1
            if coin in range(amount+1):
                dp[coin] = 1
        
        #Loop through and update DP array.
        for i in range(1,amount+1):

            #Loop through coin array and choose the coin with the smallest difference from the amount
            for coin in coins:
                difference = i - coin
                if difference > 0: #Means I can take a coin
                    dp[i] = min((dp[i-coin] + 1),dp[i])
        
        print(dp)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]