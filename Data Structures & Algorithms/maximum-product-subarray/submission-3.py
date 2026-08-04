class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #Create a dp array that stores maximum product seen at each index
        #Base Case, index 0, product of itself
        dp = [(0,0)] * len(nums)
        dp[0] = (nums[0],nums[0])
        globalMax = -float('inf')

        if len(nums) == 1:
            return nums[0]

        #Keep track of current minimum and current maximum
        for i in range(1,len(nums)):
            #Compare previous product and number by itself
            productMax = nums[i] * dp[i-1][0]
            productMin = nums[i] * dp[i-1][1]
            
            curMax = max(productMax,productMin,nums[i])
            curMin = min(productMax,productMin,nums[i])
            globalMax = max(curMax,curMin,globalMax)
            
            dp[i] = (curMax,curMin)

        return globalMax
        