class Solution:
    def rob(self, nums: List[int]) -> int:
        #Choice: rob or dont rob
        #dp array: maximum money that you can get at each robbed house
        #At each step, you can rob the current house or previous house
        maxMoney = 0
        dp =  [0] * len(nums)

        if len(nums) < 2:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        maxMoney = max(dp[0],dp[1])

        #At each step, max of (i-2 + cur) or i-1
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], (dp[i-2] + nums[i]))
            maxMoney = max(maxMoney,dp[i])
        print(dp)
        return maxMoney