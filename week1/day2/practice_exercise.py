# task: Write a program that asks the user to enter a string.

# If the string has an odd length: Reverse it and convert all characters to uppercase.
# If the string has an even length: Create a new string of the same length, repeating the first and last characters of the original string (in lowercase) as many times as needed.
# Print the resulting string.

text=input("please input a string: ")

if len(text) % 2 != 0:
    result=text[::-1].upper()
else:
    
    result = ""
    for i in range(0, len(text)//2):
        #print(text[0].lower())
        result += (text[0]+text[-1]).lower()
    result2 = (text[0]+text[-1]).lower()*(len(text)//2)
print(result)
print(result2)