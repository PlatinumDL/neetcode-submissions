class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow] #Go to index in list
            fast = nums[nums[fast]] #Move twice, go to nums[fast] first, then go to nums[of that]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow

        