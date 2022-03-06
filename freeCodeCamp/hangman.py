import random
import string

print(string.Formatter().format('ads'))
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

class Hangman:
    def __init__(self):
        self.accountant = 0
        self.ITEMS = ['Computadora','pc','boligrafo','raton','teclado','monitor','linux','qtile']
        self.AHORCADO = AHORCADO
        self.listLetter = []
    
    def itemSeparate(self):
        return list(random.choice(self.ITEMS))
    
    def autoListItem(self, lenItem):
        for _ in range(0,lenItem):
            self.listLetter.append('_')

    def shearchReplace(self, lenItem, letter, listLetter):
        for i in range(0,lenItem):
            if letter == listLetter[i]:
                self.listLetter[i] = letter
        if letter not in listLetter:
            self.accountant += 1

    def run(self):
        item = self.itemSeparate()
        self.autoListItem(len(item))
        while '_' in self.listLetter:
            letter = input('Enter one letter: ').lower()
            self.shearchReplace(len(item), letter, item)
            print(self.AHORCADO[self.accountant])
            print(f'Life: {6 - self.accountant}')
            print(self.listLetter)

            if self.accountant == 6:
                break

        if '_' in self.listLetter:
            return f'You lose, Correct answer:\n{item}'
        else:
            return f'Congratulation you won!!!'
            


asd = Hangman()
print(asd.run())
