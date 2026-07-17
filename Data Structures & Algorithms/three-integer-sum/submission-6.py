class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputList = []
        nums.sort()
        print(nums)
        
        #Initial Loop (pointer 1)
        for i in range(len(nums)):
            #Get target
            target = 0 - nums[i]
            pointerA = i + 1
            pointerB = len(nums) - 1
            
            #Loop two
            while pointerA < pointerB and pointerA < len(nums):
                if nums[pointerA] + nums[pointerB] == target:
                    outputList.append([nums[i], nums[pointerA] , nums[pointerB]])
                    pointerA += 1
                elif nums[pointerA] + nums[pointerB] > target:
                    pointerB -= 1
                elif nums[pointerA] + nums[pointerB] < target:
                    pointerA += 1
        
        #Remove duplicates
        print(outputList)
        for i in range(len(outputList)):
            j = i + 1
            while j < len(outputList):
                if outputList[i] == outputList[j]:
                    outputList.pop(i)
                    continue
                j += 1
        
        return outputList
