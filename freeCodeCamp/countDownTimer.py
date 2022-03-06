import time

def countDown():
    segundos = int(input('Enter seconds: '))
    while segundos >= 0:
        time.sleep(1)
        print(f'{segundos}')
        segundos -= 1

countDown()