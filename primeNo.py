# Write a Python program to check if a number is prime

def checkPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if(n % i == 0):
            return False
        else:
            return True
    

numb = int(input("Enter your number : "))

res = checkPrime(numb)
if res:
    print(f"{numb} is a prime no.")
else:
    print(f"{numb} is not a prime no.")
