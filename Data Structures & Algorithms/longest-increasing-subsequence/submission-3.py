class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) 

        #Idea: store the longest increasing subsequence at each index
        #Check previous number to see if smaller or larger. If larger, do not increase. If smaller, increase by 1

        dp[len(nums)-1] = 1 #First index by itself can be 1 increasing

        for i in range(len(nums)-1,-1,-1):
            LIS = 0
            for j in range(i+1, len(nums)):   
                cur = nums[j]
                if nums[i] < cur: #Can take
                    dp[i] = max(dp[i], (1+dp[j]))

        print(dp)
        return max(dp)