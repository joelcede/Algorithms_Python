import random

#Decorador
def quantityOfCards(func):
    def creditCars(number):
        return func(number)
    return creditCars

@quantityOfCards
def randomCard(range):
    card = str(random.randint(4,5))
    while (len(card) <= range):
        card += str(random.randint(0,9))
    return card

if __name__ == "__main__":
    card = randomCard(15)
    print("VISA: "+card if (card[0] == "4") else "MASTERCARD: "+card)
