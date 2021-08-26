# If the function receives 25, it should return TRUE, because 5^2 = 25 If the function receives 1, 
# it should return TRUE, because 1^2 = 1 If the function receives 16, 
# it should return TRUE, because 4^2 = 16 If the function receives 14, it should return FALSE.
# Limitation: 
# You CAN’T use functions of square roots (sqrt() or similar), potentiation (pow() or similar). 
# ONLY the basic arithmetic operations (sum, substraction, multiplication, division), 
# and any logic operations are allowed.

def shear(number: int) -> int:
    if number > 0:
        for i in range(10):
            if (i*i) == number:return True
            else: continue
        return False
    else: return "The number is negative!!"
        

print(shear(-2))

#deficient?