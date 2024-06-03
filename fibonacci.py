# Write a Python program to print the Fibonacci sequence up to n terms.

def fibPattern(n):
    num1, num2 = 0, 1

    print(num1, end= " ")
    print(num2, end= " ")
    for i in range (n):
        sm = num1 + num2
        print(sm, end = " ")
        num1, num2 = num2, sm


num = int(input("Enter the range of fibonacci series : "))
fibPattern(num)