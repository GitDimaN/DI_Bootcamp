# Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

list1 = [1,2,3,4]
list2 = ['a','b','c','d']

my_list = list1 + list2
print(my_list)
my_list = list1
my_list.extend(list2)
print(my_list)

# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500,2501):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

# Exercise 3: Check the index
# Instructions
# Using this variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first
# occurence of the name.

# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("please insert your name: ")
if user_name in names:
    print(names.index(user_name))

for k in range(0,len(names)):
    if user_name == names[k]:
        print(k)
        
# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

user_nums = []
for i in range(1,4):
    user_nums.append(float(input(f"input the {i} number: ")))
print(f"The greatest number is {max(user_nums)}")


# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter 
# and whether its a vowel or a consonant.

# quick print using string:
import string
alphabet = list(string.ascii_lowercase)
print(",".join(alphabet))  # ['a', 'b', ..., 'z']

# via looping
for l in alphabet:
    if l in "aeiou":
        print(f"{l} is a vowel")

