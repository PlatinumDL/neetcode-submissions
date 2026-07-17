class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        #Evaluate from the back
        outputArr = [0] * len(temperatures)
        outputArr[len(temperatures)-1] = 0

        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            while len(stack) > 0 and curTemp > stack[-1][0]:
                #Relinquish Stacks
                difference = i - stack[-1][1]
                outputArr[stack[-1][1]] = difference
                stack.pop()

            #Append to stack
            stack.append((curTemp,i)) 
        
        return outputArr


        