def isPalindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(isPalindrome(43))

if __name__ == '__main__':
    run()
