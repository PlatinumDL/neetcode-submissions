class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #I can move ONE or TWO steps by paying the cost
        #The cost is retrieved from the cost array
        dp = [0] * (len(cost) + 1)

        dp[0] = 0
        dp[1] = 0
        if len(cost) < 2:
            return 0
        dp[2] = min(cost[0],cost[1])

        for i in range(3,len(cost)+1):
            #A steps cost is dependent on the minimum cost between the prev two steps
            dp[i] = min(
                (dp[i-1] + cost[i-1])
                ,(dp[i-2] + cost[i-2])
                )
        print(dp)
        print(cost)
        return dp[len(cost)]