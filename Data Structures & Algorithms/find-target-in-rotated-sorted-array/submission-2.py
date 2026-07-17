class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0

        while start < end:
            middle = (start + end) // 2
            #Split point is inside [start, end]
            if nums[middle] > nums[end]: #Split point is after middle
                start = middle + 1
            else: #Split point is middle or before middle
                end = middle
        split = start
        print(split)
        
        #With split point, check if target is above or below split point, then do binary search for target
        if target < nums[0] or split == 0: #Target is after split point
            start = split
            end = len(nums) - 1
            while start <= end: #Target is inside [start,end]
                middle = (start + end) // 2
                if nums[middle] == target: #Found target
                    return middle
                elif nums[middle] > target:
                    end = middle - 1
                else:
                    start = middle + 1

        else: #Target is before split point
            start = 0
            end = split - 1
            while start <= end: #Target is inside [start,end]
                middle = (start + end) // 2
                if nums[middle] == target: #Found target
                    return middle
                elif nums[middle] > target:
                    end = middle - 1
                else:
                    start = middle + 1

        return -1 #not found, return -1