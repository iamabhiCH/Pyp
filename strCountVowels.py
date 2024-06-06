# Write a Python program to count the number of vowels in a string.

def countVowels(str):
    cnt = 0

    for i in str:
        if i.lower() in 'aeiou':
            cnt += 1
        elif i in 'AEIOU':
            cnt += 1
    
    return cnt

str = input("Enter the string : ")
print("Number of vowels in the string is : ", countVowels(str))