from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = {}
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                #Append all the treasures for BFS
                if grid[row][col] == 0:
                    queue.append((row,col))

        while len(queue) > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                directions = [[row-1,col], [row+1,col], [row,col-1], [row,col+1]]
                for nrow, ncol in directions:
                    if nrow in range(rows) and ncol in range(cols) and grid[nrow][ncol] == 2147483647:
                        queue.append((nrow,ncol))
                        grid[nrow][ncol] = grid[row][col] + 1

        