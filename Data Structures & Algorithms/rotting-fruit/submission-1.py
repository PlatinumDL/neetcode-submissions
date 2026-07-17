class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        minutes = 0
        fresh = 0

        #Edge Cases -> grid empty
        if grid == None:
            return -1

        #Add all the rotten fruits into the queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1


        #With all the rotten fruits in the queue, commence BFS
        while len(queue) > 0 and fresh > 0:
            #update minutes
            minutes += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                directions = [[row-1,col], [row+1,col], [row,col-1], [row,col+1]]
                for nrow, ncol in directions:
                    #Only want to move towards fresh fruit
                    if nrow in range(rows) and ncol in range(cols) and grid[nrow][ncol] == 1:
                        #change fruit to rotten and push to queue
                        grid[nrow][ncol] = 2
                        fresh -= 1
                        queue.append((nrow,ncol))

        #Check if any fruits left are fresh
        if fresh != 0:
            return -1
        
        return minutes