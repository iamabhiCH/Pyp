# Write a Python program to perform addition, subtraction, multiplication, division, and modulo of two numbers.

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

sm = num1 + num2
print(sm)

sb = num1 - num2
print(sb)

ml = num1 * num2
print(ml)

if(num2 != 0):
    dv = num1 / num2
    print(sb)
else:
    print("Error! Please enter number greater than 1.")

if(num2 != 0):
    md = num1 % num2
    print(md)
else:
    print("Error! Please enter the number greater than 1.")
