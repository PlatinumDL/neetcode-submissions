class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMaxVolume = 0
        #Select first height 
        leftContainer = 0
        rightContainer = len(heights) - 1

        while leftContainer < rightContainer:
            #Width
            width = rightContainer - leftContainer
            print(width)
            #Height 
            height = min(heights[rightContainer],heights[leftContainer])
            #Volume
            volume = width * height 
            #Update
            if volume > currentMaxVolume:
                currentMaxVolume = volume

            #Move pointers -> Move the smaller pointer
            if heights[rightContainer] < heights[leftContainer]:
                rightContainer -= 1
            elif heights[leftContainer] <= heights[rightContainer]:
                leftContainer += 1

        return currentMaxVolume
        