class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = {}


        def dfs(row,col,area):
            #Update max area on every iteration
            
            directions = [[row-1,col], [row+1,col], [row,col-1], [row,col+1]]
            for row, col in directions:
                if row in range(rows) and col in range(cols) and visited.get((row,col)) == None and grid[row][col] == 1:
                    visited[(row,col)] = 1
                    area = max(area,dfs(row,col,area+1))
            
            return area

        for row in range(rows):
            for col in range(cols):
                #Check if tile is land and not visited yet
                if grid[row][col] == 1 and visited.get((row,col)) == None:
                    #Run DFS on the tile and set visited
                    visited[(row,col)] = 1
                    maxArea = max(maxArea,dfs(row,col,1)) #Area = 1 -> one tile island


        return maxArea