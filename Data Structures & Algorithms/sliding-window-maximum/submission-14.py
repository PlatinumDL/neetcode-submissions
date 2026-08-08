class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Maintain a heapq at each iteration
        #Remove and add manually from left
        output = []
        window = deque()
        window.append(nums[0])

        #Create initial window and add to output
        #Left will be max value
        for i in range(1,k):
            cur = nums[i]
            while len(window) > 0 and cur > window[-1]:
                window.pop()
            window.append(cur)
        output.append(window[0])

        left = 0
        for i in range(k,len(nums)):
            #Get current number
            cur = nums[i]
            
            if nums[left] == window[0]: #Maximum is left, need Remove
                window.popleft()

            #If new number is the new maximum
            while len(window) > 0 and cur > window[-1]:
                window.pop()
            window.append(cur)
            
            #Append maximum value to output
            left += 1
            output.append(window[0])
        
        
        return output
        
