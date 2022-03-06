import random

def is_win(p, o):
    if(p == 'r' and o == 's') or (p == 's' and o == 'p') or (p == 'p' and o == 'r'):
        return True

def play():
    user = input('choice [r, s or p]: ')
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'dead heat'

    if (user != 'r') and (user != 's') and (user != 'p'):
        return 'No matches'

    if is_win(user, computer):
        return 'Win user'
    return 'win computer'

print(play())