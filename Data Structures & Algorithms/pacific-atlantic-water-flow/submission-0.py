class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Idea -> Store nodes bordering pacific and atlantic into a dictionary
        pacific = {}
        atlantic = {}
        visited = {} #Atlantic
        visitedPacific = {}
        output = []
        rows = len(heights)
        cols = len(heights[0])
        
        #Add horizontal
        for counter in range(cols):
            pacific[(0,counter)] = 1
            atlantic[(len(heights)-1,counter)] = 1

        #Add Vertical
        for counter in range(rows):
            pacific[(counter,0)] = 1
            atlantic[(counter,len(heights[0])-1)] = 1

        def dfs(row,col,ocean):
            #Directions to traverse
            directions = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
            
            if ocean == "atlantic":
                visited[(row,col)] = 1
            elif ocean == "pacific":
                visitedPacific[(row,col)] = 1

            for nrow, ncol in directions:
                if ocean == "atlantic":
                    if nrow in range(rows) and ncol in range(cols) and visited.get((nrow,ncol)) != 1 and heights[nrow][ncol] >= heights[row][col]:
                        dfs(nrow,ncol,ocean)
                elif ocean == "pacific":
                    if nrow in range(rows) and ncol in range(cols) and visitedPacific.get((nrow,ncol)) != 1 and heights[nrow][ncol] >= heights[row][col]:
                        dfs(nrow,ncol,ocean)

        #Loop through every node in atlantic
        for key,val in atlantic.items():
            row, col = key
            #Do DFS if node is not visited yet
            if visited.get((row,col)) != 1:
                dfs(row,col,"atlantic")

        #Loop through every node in pacific
        for key,val in pacific.items():
            row, col = key
            #Do DFS if node is not visited yet
            if visitedPacific.get((row,col)) != 1:
                dfs(row,col,"pacific")

        #Loop through each node and check
        for row in range(rows):
            for col in range(cols):
                if visited.get((row,col)) == 1 and visitedPacific.get((row,col)) == 1:
                    output.append([row,col])

        return output