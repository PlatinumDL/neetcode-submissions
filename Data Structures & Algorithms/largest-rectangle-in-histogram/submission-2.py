class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestSeen = 0
        stack = []
        stack.append((heights[0],0))
        counter = 1
        indexToPut = 1
        #Iterate through list and settle stack
        while stack and counter < len(heights):
            indexToPut = counter
            #print(stack)
            while stack and stack[-1][0] > heights[counter]:
                #Pop stack and calculate max area for that bar
                topHeight, topIndex = stack.pop()
                difference = counter - topIndex
                indexToPut = topIndex
                area = topHeight*difference
                if area > largestSeen:
                    largestSeen = area
            stack.append((heights[counter],indexToPut))
            counter += 1
        while stack:
            topHeight, topIndex = stack.pop()
            area = topHeight * (len(heights) - topIndex)
            largestSeen = max(largestSeen, area)
        
        return largestSeen




    
            



        
        