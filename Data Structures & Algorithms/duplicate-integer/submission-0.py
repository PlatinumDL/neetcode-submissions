class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1 Loop -> Add to hashtable if doesnt exist. If exist, return true
        #End of loop -> return false
        numDict = {}
        for i in range(len(nums)):
            temp = numDict.get(nums[i])
            if temp is not None:
                return True
            numDict.update({nums[i]:1})
        return False