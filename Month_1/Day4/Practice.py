#Functin to chect prime
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

n = int(input("Enter a number:"))

if is_prime(n):
    print("prime number")
else:
    print("Not a prime number")


#function to reverse string
def rev_string(txt):
    return txt[::-1]

txt = input("Enter String:")
print("Reversed string:",rev_string(txt))


#Function to calculate factorial
def factorial1(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

n1 = int(input("Enter a number:"))
print("Factorial number:",factorial1(n1))