class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Loop through the array of integers
        #Initialize a hashtable
        #Every loop, subtract nums[i] from target and add remainder to hashtable
        #If remainder exists in hashtable, return true
        diffDict = {}
        
        for i in range(len(nums)):
            #Get Difference
            difference = target - nums[i]
            #Check if difference is inside dict
            if difference in diffDict:
                #If difference inside dict, get index and return
                diffIndex = diffDict.get(difference)
                return [diffIndex,i]
            else:
                diffDict[nums[i]] = i
        
        return []