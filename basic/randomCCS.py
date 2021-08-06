import random

# Applying static typing, closure and decorator
def quantityOfCards(func):
    def creditCards(number: int) -> str:
        return func(number)
    return creditCards

# Generate randoms CC(visa or mastercard)
@quantityOfCards
def randomCard(range: int) -> str:
    card = str(random.randint(4,5))
    while (len(card) <= range):
        card += str(random.randint(0,9))
    return card

if __name__ == "__main__":
    card = randomCard(15)
    print("VISA: " + card if (card[0] == "4") else "MASTERCARD: " + card)
