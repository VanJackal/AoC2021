import numpy as np

class Board:
    def __init__(self,board):
        self.board = board
        self.x = len(board)
        self.y = len(board[0])
        self.called = np.zeros((self.x, self.y))
    
    def call(self, num):
        for i in range(self.x):
            for j in range(self.y):
                if self.board[i][j] == num:
                    self.called[i,j] = 1
    
    def printBoard(self):
        for i in range(self.x):
            for j in range(self.y):
                suffix = "*" if self.called[i,j] else ""
                print(str(self.board[i][j]) + suffix,end=" ")
            print()
    
    def checkBoard(self):
        for row in self.called:
            if np.all(row):
                return True
        
        for col in np.transpose(self.called):
            if np.all(col):
                return True

        return False
    
    def getUncalledSum(self):
        total = 0
        for i in range(self.x):
            for j in range(self.y):
                if not self.called[i,j]:
                    total += self.board[i][j]
        return total