# Write a Python program to remove all whitespace characters from a string.

def removeSpaces(str):
    return str.replace(" ","")

str1 = input("Enter your string : ")
str2 = removeSpaces(str1)
print(str2)