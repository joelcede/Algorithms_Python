import random

def computer(number):
    randomNumber = random.randint(1, number)
    pc = 0
    while pc != randomNumber:
        pc = int(input(f'Choice a number betwenn 1 and {number}: '))
        if randomNumber < pc:
            print('The number is small')
        elif randomNumber > pc:
            print('the number is big')
    print(f'The pc a computer is equal {pc}')

def user(number):
    randomNumber = random.randint(1, number)
    user = 0
    while user != randomNumber:
        user = int(input(f'Choice a number betwenn 1 and {number}: '))
        if randomNumber < user:
            print('The number is small')
        elif randomNumber > user:
            print('the number is big')
    print(f'The user a computer is equal {user}')

computer(6)
print()
user(6)