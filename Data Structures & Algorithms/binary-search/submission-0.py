class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            value = nums[int(middle)]
            #If target is smaller, search first half
            #If target is larger, search second half
            if target == value:
                return int(middle)
            elif target < value:
                end = middle - 1
            elif target > value:
                start = middle + 1   
        return -1