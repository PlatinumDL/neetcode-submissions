class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edgeO = {}
        visited = {}

        #DFS Solution: Go through the edge of the board, and add all O to edgeO.
        #Do BFS on the edgeO, and add it to visited.
        #Replace all O that is not in visited with X

        rows = len(board)
        cols = len(board[0])

        for col in range(cols):
            if board[0][col] == "O":
                edgeO[(0,col)] = 1
            if board[rows-1][col] == "O":
                edgeO[(rows-1,col)] = 1

        for row in range(rows):
            if board[row][0] == "O":
                edgeO[(row,0)] = 1
            if board[row][cols-1] == "O":
                edgeO[(row,cols-1)] = 1
        
        print(edgeO)

        def dfs(row,col):
            #Set visited
            visited[(row,col)] = 1
            directions = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
            for nrow,ncol in directions:
                if nrow in range(rows) and ncol in range(cols) and visited.get((nrow,ncol)) == None and board[nrow][ncol] == "O":
                    dfs(nrow,ncol)

        #For each O on the edge
        for key,val in edgeO.items():
            row, col = key
            dfs(row,col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and visited.get((row,col)) == None:
                    board[row][col] = "X"


