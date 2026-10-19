# Challenge 1: Multiples of a Number
# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

# Example 1:

# Input:

# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]

number = int(input("input a desired number: "))
length = int(input("input the desired length of the list containing its multiples: "))

multiples_list = []
for i in range (1, length+1):
    multiples_list.append(i*number)
print(f"list of multiples: {multiples_list}")

# Challenge 2: Remove Consecutive Duplicate Letters
# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.



# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"

initial_str = input("insert your string: ")
print(f"your string is: {initial_str}")
new_str = initial_str[0]

for i in range(1, len(initial_str)):
    if initial_str[i] != initial_str[i-1]:
       new_str += initial_str[i]
print(f"the new string is: {new_str}")