# Write a Python program to calculate the factorial of a number.

def findFactorial(n):
    if n == 0: 
        print("The factorial of",n,"is 1.")
        return

    fct = 1
    for i in range (n):
        fct += fct * i
    
    print(f"The factorial of {n} is {fct}")
    return

num = int(input("Enter your number to find factorial : "))
findFactorial(num)