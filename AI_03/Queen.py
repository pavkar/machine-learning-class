class NQPosition:
    
    def __init__(self, N):
        self.N = N
        self.answer = []
        self.answerFound = False
        positions = [-1] * self.N
        self.findQueenPlace(positions, 0)

    def findQueenPlace(self, positions, currentRow):
        if currentRow != self.N:
            for column in range(self.N):
                if self.canPlaceQueen(positions, currentRow, column):
                    positions[currentRow] = column
                    
                    if not(self.checkPositions(positions)):
                        self.findQueenPlace(positions, currentRow + 1)
                    elif not(self.answerFound):
                        self.answerFound = True
                        self.answer = positions
                        
                        print ("Answer: ")
                        print(self.answer)
                        print("")
                        self.printAnswer()
                        break

    def canPlaceQueen(self, positions, currentRow, column):
        for i in range(currentRow):
            if positions[i] == column or positions[i] - i == column - currentRow or positions[i] + i == column + currentRow:
                return False
        return True
    
    def checkPositions(self, positions):
        for p in positions:
            if p == -1:
                return False
        return True
    
    def printAnswer(self):
        printedAnswer = ["-"] * N
        
        for n in range(N):
            printedAnswer[n] = ["-"] * N
        
        for y in range(N):
            for x in range(N):
                if self.answer[x] == y:
                    printedAnswer[x][y] = "Q"
        
        for l in printedAnswer:
            print(l)
        
if __name__ == "__main__":
    N = 5
    NQPosition(N)

