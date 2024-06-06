# Write a Python program to check if a string is a palindrome.

def checkPalindrome(str):
    return str == str[::-1]

str = input("Enter your string : ")
s = checkPalindrome(str)

if s:
    print("Yes")
else:
    print("No")