class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Loop through the array once
        #Two pointers, one from the back and one from the front
        left = 0
        right = len(numbers) - 1

        #During every loop, sum the left and right pointer. If it is larger than the target, move right pointer - 1. If smaller, move left pointer up
        for i in range(len(numbers)):
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            if sum < target:
                left += 1
            if sum == target:
                return [left+1,right+1]
        