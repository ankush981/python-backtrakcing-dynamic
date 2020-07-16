# Give an n x n chess board and n queen pieces, our goal is to place all the queens on the board such that none of them attacks any other queen. The "not attack any other" is the constraint in this "constraint specification problem". :)

class QueensProblem:
    def __init__(self, numOfQueens):
        self.numOfQueens = numOfQueens
        self.chessboard = [[None for i in range(numOfQueens)] for j in range(numOfQueens)]
    
    def solveQueensProblem(self):
        if self.numOfQueens < 4:
            print("Invalid problem size")
        elif self.solve(0): # start with the first column and see if solve() returns True
            self.printQueens()
        else:
            print("There is no solution")
        
    def solve(self, colIndex):
        if colIndex == self.numOfQueens: # cols go from 0 to 7, so for 8th column, all 8 queens already placed and problem solved
            return True
        
        for rowIndex in range(self.numOfQueens): # we iterate over rows here  because within a column, we only consider the placement of queens row-wise (top to bottom)
            if self.isPlaceValid(rowIndex, colIndex):
                # place a queen here
                self.chessboard[rowIndex][colIndex] = 1

                # if with this placement, we are able to solve for the next colmun, we have made a good choice and the problem is solved "for this column"
                if self.solve(colIndex + 1):
                    return True
                
                # otherwise, the earlier placement of the queen was wrong, so we reset it and go back to the next row (as dictated by the loop)
                self.chessboard[rowIndex][colIndex] = 0
        
        # we've run out of squares on the first column to place the first queen
        return False
    
    def isPlaceValid(self, rowIndex, colIndex):
        # check if placing a new queen causes two queens to be in the same row
        for i in range(colIndex):
            if self.chessboard[rowIndex][i] == 1:
                return False
        
        # check if new queen falls on a top-left to bottom-right diagonal with another queen
        j = colIndex
        for i in range(rowIndex, -1, -1): # row-- means move the scan up from current row to zero
            if j < 0:
                break
            
            if self.chessboard[i][j] == 1:
                return False
            
            j = j - 1 # move the scan back

        # check if new queen falls on a bottom-left to top-right diagonal with another queen
        j = colIndex
        for i in range(rowIndex, len(self.chessboard)): # move the scan down from current row to max
            if j < 0:
                break
            
            if self.chessboard[i][j] == 1:
                return False
            
            j = j - 1 # notice that there's a decrement in j (colIndex) in both the cases because we are checking whether the new queen attacks any of the queens placed previously (in the earlier, lower-indexed columns)

        return True
    
    def printQueens(self):
        for i in range(self.numOfQueens):
            for j in range(self.numOfQueens):
                if self.chessboard[i][j] == 1:
                    print(' * ', end = '')
                else:
                    print(' - ', end = '')
            print('\n')

if __name__ == "__main__":
    queensProblem = QueensProblem(8)
    queensProblem.solveQueensProblem();
    queensProblem.printQueens()
