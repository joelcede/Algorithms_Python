import random

class TicTacToe:
    def __init__(self):
        self.XCPU = 'X'
        self.OPERSON = 'O'
        self.BOARD = []
        self.rangeBoard = 3
        self.turnPerson = bool()
        self.won = bool()
    
    def board(self):
        #board 3x3
        for i in range(self.rangeBoard):
            self.BOARD.append([])
            for _ in range(self.rangeBoard):
                self.BOARD[i].append(' ')
        return self.BOARD

    def turnCPU(self, board):
        coordinates = []
        for i in range(self.rangeBoard):
            for j in range(self.rangeBoard):
                if board[i][j] == ' ':
                    coordinates.append([i, j])
        return random.choice(coordinates)

    def containBoard(self, board):
        # isFalseList = []
        for i in range(self.rangeBoard):
            if ' ' not in board[i]:
                # isFalseList.append(True)
                return True
        # return isFalseList
        # print(isFalseList)

    def winRow(self, board, player):
        for i in range(self.rangeBoard):
            for j in range(self.rangeBoard):
                # print(board[i][j] ,i, j)
                if board[i][j] == player: self.won = True
                else: 
                    self.won = False 
                    break
            if self.won ==  True: break
        return self.won
        # print(self.won)

    def winColumn(self, board, player):
        for i in range(self.rangeBoard):
            for j in range(self.rangeBoard):
                # print(board[j][i], j, i)
                if board[j][i] == player: self.won = True
                else:
                    self.won = False
                    break
            if self.won == True: break
        return self.won

    def winTiltedRight(self, board, player):    
        for i in range(self.rangeBoard):
            # print(board[i][i], i, i)
            if board[i][i] == player: self.won = True
            else:
                self.won = False
                break
        return self.won

    def winTiltedLeft(self, board, player):
        ran = self.rangeBoard
        for i in range(self.rangeBoard):
            # print(board[i][ran - i - 1], i, ran - i - 1)
            if board[i][ran-i-1] == player: self.won = True
            else:
                self.won = False
                break
        return self.won

    def winnerLogic(self, board, win):
        # self.turnCPU()
        # self.board()
        # bWin = self.BOARD
        logica = bool()
        if self.winRow(board, win) == True: logica = True
        elif self.winColumn(board, win) == True: logica = True
        elif self.winTiltedLeft(board, win) == True: logica = True
        elif self.winTiltedRight(board, win) == True: logica = True
        else: logica = False
        return logica
        
