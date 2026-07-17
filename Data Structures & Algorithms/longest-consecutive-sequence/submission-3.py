class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a dictionary
        # Loop through the array ONCE

        # Everytime a number is processed, check if +1 or -1 is in the dictionary. If it is add it to the dictionary and increment counter
        # Dictionary key = number, value = consecutive
        numsDict = defaultdict(int)
        longest = 0

        for j in range(len(nums)):
            if not numsDict[nums[j]]:
                # Not inside, it bridges the gap
                # Left + 1 + right
                length = numsDict[nums[j] - 1] + 1 + numsDict[nums[j] + 1]
                numsDict[nums[j]] = length
                numsDict[nums[j] - numsDict[nums[j] - 1]] = length
                numsDict[nums[j] + numsDict[nums[j] + 1]] = length
                longest = max(length, longest)

        return longest
