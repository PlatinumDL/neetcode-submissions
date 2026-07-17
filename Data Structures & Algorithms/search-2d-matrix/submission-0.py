class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #First, find which row it is in
        start = 0
        end = len(matrix) - 1
        row = 0
        #Get first index to check
        while start <= end:
            middle = (start+end) // 2
            value = matrix[middle][0]
            
            if target == value:
                return True
            elif target < value:
                end = middle - 1
            elif target > value:
                start = middle + 1
        
        row = end
        start = 0
        end = len(matrix[row]) - 1
        
        #Binary search on index row
        while start <= end:
            middle = (start+end) // 2
            value = matrix[row][middle]
            if value == target:
                return True
            elif target < value:
                end = middle - 1
            elif target > value:
                start = middle + 1
        
        return False
