class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        numZeros = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                numZeros += 1
            else:
                totalProduct = totalProduct * nums[i]
        
        outputArr = []
        for j in range(len(nums)):
            if nums[j] == 0 and numZeros == 1:
                outputArr.append(totalProduct)
            elif numZeros > 1:
                outputArr.append(0)
            elif nums[j] != 0 and numZeros == 1:
                outputArr.append(0)
            else:
                temp = int(totalProduct / nums[j])
                outputArr.append(temp)

        return outputArr

        