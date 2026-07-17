class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = len(speed)
        combinedArr = []
        for i in range(len(position)):
            combinedArr.append((position[i], speed[i]))
        combinedArr.sort()
        #print(combinedArr[-1][0])

        for i in range(1,len(position)+1):
            timeAtDestination = (target - combinedArr[-i][0]) / combinedArr[-i][1]
            print(timeAtDestination)
            if len(stack) > 0:
                if timeAtDestination <= stack[-1]:
                    fleet -= 1
                else:
                    #This means that they dont intersect 
                    stack.pop()
                    stack.append(timeAtDestination)
            else:
                stack.append(timeAtDestination)

        return fleet


        