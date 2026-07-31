class Solution:
    def rob(self, nums: List[int]) -> int:
        #Cannot rob two adjacent houses. #Last and first element are adjacent
        #I do DP twice? Once clockwise and once anti-clockwise
        dp = [0] * len(nums)
        dp2 = [0] * len(nums)
        if len(nums) < 2:
            return max(nums)

        #DP clockwise (take first value)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1],(nums[i] + dp[i-2]))
        print(dp)

        dp2[0] = nums[-1]
        dp2[1] = max(nums[-1],nums[-2])
        for i in range(2,len(nums)-1):
            dp2[i] = max(dp2[i-1], (nums[-(i+1)] + dp2[i-2]))
        print(dp2)

        return max(max(dp),max(dp2))