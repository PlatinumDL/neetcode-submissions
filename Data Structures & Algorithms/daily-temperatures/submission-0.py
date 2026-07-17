class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Idea -> Two Stacks, Count number of pops from the second stack for "number of warmer temps"
        stack = []
        outputList = [0] * len(temperatures)
        stack.append((temperatures[0],0))
        counter = 1

        while counter < len(temperatures):
            #Check if cur temp is larger than top temp
            curTemp = temperatures[counter]

            while len(stack) > 0 and curTemp > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                differenceDays = counter - topIndex
                outputList[topIndex] = differenceDays
            
            stack.append((curTemp,counter))
            counter += 1

        return outputList    