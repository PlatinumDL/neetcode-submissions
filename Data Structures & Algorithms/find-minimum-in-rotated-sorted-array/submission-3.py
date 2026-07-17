class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Find the split point
        #Then do binary search on both splits
        start = 0
        end = len(nums) - 1
        split = 0
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        
        while start < end:
            #[start, end] -> split point is still inside
            middle = (start + end) // 2
            #If middle is larger than end, something is WRONG -> split point is in second half [middle+1, end]
            if nums[middle] > nums[end]:
                start = middle + 1
            #Middle is smaller than end -> split point in the first half  [start, middle-1]
            else:
                end = middle 
        #Split Point
        return nums[start]