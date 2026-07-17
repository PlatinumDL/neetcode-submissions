class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        #bfs
        def bfs(row,col):
            #up, down, left, right
            directions = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
            #run bfs for each direction
            for row,column in directions:
                #Check if within bounds and whether already visited
                if row in range(rows) and column in range(cols) and visited.get((row,column)) == None and grid[row][column] == "1":
                    #Updated visited
                    visited[(row,column)] = 1
                    bfs(row,column)
        
        
        #For each row loop
        for row in range(rows):
            #For each col loop
            for col in range(cols):
                cur = grid[row][col]
                #Check if it is already visited
                if cur == "1" and visited.get((row,col)) == None:
                    #Add to visited, run bfs search and increment islands
                    visited[(row,col)] = 1
                    #bfs
                    bfs(row,col)
                    islands += 1
        
        return islands

