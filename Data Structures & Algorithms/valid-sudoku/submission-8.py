class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        boxes = {}

        #Initialize boxes
        for i in range(length//3):
            for j in range(length//3):
                boxes[i,j] = {}

        #For each row - loop
        for i in range(length):
            #hashtable for row
            rowDict = {}
            columnDict = {}

            for j in range(length): 

                #Check if row value is in rowDict
                if board[i][j] not in rowDict:
                    if board[i][j] != ".":
                        rowDict[board[i][j]] = 1
                else:
                    return False
                
                #Check if column value is in columnDict
                if board[j][i] not in columnDict:
                    if board[j][i] != ".":
                        columnDict[board[j][i]] = 1
                else:
                    return False

                #Check if boxValue is in boxDict
                newi = i//3
                newj = j//3
                if board[i][j] not in boxes[newi,newj]:
                    if board[i][j] != ".":
                        boxes[newi,newj][board[i][j]] = 1
                else:
                    return False

        return True

                
            

        