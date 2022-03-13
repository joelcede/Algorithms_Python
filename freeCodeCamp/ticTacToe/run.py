from logic import TicTacToe
import os


class PlayTicTacToe(TicTacToe):
    def __init__(self):
        TicTacToe.__init__(self)

    def verInt(self, text):
        while True:
            try:
                pos = int(input(text))
                if pos < self.rangeBoard: return pos
                else: 
                    print('Elige un numero menor')
                    continue
                break
            except:
                os.system('clear') 
                print('Write a number')
        # return pos 

    def play(self):
        xd = self.board()
        while self.won == False:

            if self.turnPerson == False:
                if self.won == False:
                    move = self.turnCPU(xd)
                    self.BOARD[move[0]][move[1]] = self.XCPU
                    self.turnPerson = True
                winner = self.winnerLogic(self.BOARD, self.XCPU)
                if winner: 
                    print('GANADOR MAQUINA')
                    self.won = True
            else:
                if self.won == False:
                    winner = self.winnerLogic(self.BOARD, self.OPERSON)
                    print(f'winner person: {winner}')
                    if winner: self.won = True
                    else:
                        # print(self.BOARD)
                        turnPersonY = self.verInt(f'Y: Enter a number from 0 to {self.rangeBoard-1}: ')
                        turnPersonX = self.verInt(f'X: Enter a number from 0 to {self.rangeBoard-1}: ')
                        if self.BOARD[turnPersonY][turnPersonX] != ' ': 
                            # print('Ocupado')
                            continue
                        else: 
                            self.BOARD[turnPersonY][turnPersonX] = self.OPERSON
                            self.turnPerson = False
                else: print('ganador Persona')
            print(self.BOARD)
    
    def boardDraw(self, l):
        a = [f'''┌───┐ ┌───┐ ┌───┐
│ {l[0][0]} │ │ {l[0][1]} │ │ {l[0][2]} │
└───┘ └───┘ └───┘
┌───┐ ┌───┐ ┌───┐
│ {l[1][0]} │ │ {l[1][1]} │ │ {l[1][2]} │
└───┘ └───┘ └───┘
┌───┐ ┌───┐ ┌───┐
│ {l[2][0]} │ │ {l[2][1]} │ │ {l[2][2]} │
└───┘ └───┘ └───┘''']
        print(a[0])


    def play(self):
        board = self.board()
        win = ""
        coor = []
        while self.won == False:
            if self.turnPerson == True:
                turnPersonY = self.verInt(f'Y: Enter a number from 0 to {self.rangeBoard-1}: ')
                turnPersonX = self.verInt(f'X: Enter a number from 0 to {self.rangeBoard-1}: ')
                if self.BOARD[turnPersonY][turnPersonX] != ' ':
                    os.system('clear')
                    self.boardDraw(self.BOARD)
                    print('Casilla ocpada')
                    continue
                else: 
                    self.BOARD[turnPersonY][turnPersonX] = self.OPERSON
                    self.turnPerson = False
                winner = self.winnerLogic(self.BOARD, self.OPERSON)
                if winner == True:
                    win = 'Win Person'
                    self.won = True
            else:
                move = self.turnCPU(board)
                self.BOARD[move[0]][move[1]] = self.XCPU
                winner = self.winnerLogic(self.BOARD, self.XCPU)
                if winner == True:
                    win = 'Win CPU'
                    self.won == True
                self.turnPerson = True
            os.system('clear')
            self.boardDraw(self.BOARD)
            print(win)
            for i in range(self.rangeBoard):
                for j in range(self.rangeBoard):
                    if self.BOARD[i][j] == ' ':
                        coor.append([i, j])
            if coor == [] and self.won == False:
                print('Empate')
                break
            coor = []


PlayTicTacToe().play()

