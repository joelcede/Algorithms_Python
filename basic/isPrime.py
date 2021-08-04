def isPrime(prime: int) -> bool:
    return prime%2==1

def run():
    print(isPrime(12))
    print(isPrime(11))

if __name__ == "__main__":
    run()