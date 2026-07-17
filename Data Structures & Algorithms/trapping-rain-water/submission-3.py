class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        leftMax = height[left] 
        rightMax = height[right]
        
        while left < right:
            print(leftMax)
            curLeft = height[left]
            curRight = height[right]

            if leftMax <= rightMax:
                water = water + max(0, (leftMax - curLeft))
                left += 1
                if height[left] > leftMax:
                    leftMax = height[left]

            else:
                water = water + max(0, (rightMax - curRight))
                right -=1
                if height[right] > rightMax:
                    rightMax = height[right]
        return water