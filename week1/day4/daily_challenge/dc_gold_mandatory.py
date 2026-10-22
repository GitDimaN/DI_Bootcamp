# What You’ll learn
# Python Basics
# Conditionals
# Loops
# Functions
# Lists (2D lists/matrices)
# String Manipulation

# Key Python Topics:
# Strings
# Lists (2D lists)
# Loops (for loops)
# Conditional statements (if, else)
# String methods (.isalpha(), etc.)
# String concatenation.

# Instructions:
# You are given a “Matrix” string:
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''     
print(MATRIX_STR)  # This will print the original matrix string.

# This represents a grid of characters, and your task is to decode the hidden message within.

# Understanding the Matrix:

# Imagine this string arranged in rows and columns, forming a grid.
# To work with it in Python, you’ll need to transform this string into a 2D list (a list of lists), where each inner list represents a row.

# Step 1: Transforming the String into a 2D List
list_2D = [list(row) for row in MATRIX_STR.strip().split('\n')]
print(list_2D)

# to see the matrix better visually:
for row in MATRIX_STR.strip().split('\n'):
    print(list(row))

# Step 2: Processing Columns
# Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
# You’ll need to write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.

# reading as Neo:
for k in range(len(list_2D[0])):
    # col k fixed
    for i in range(len(list_2D)):
        # rows = amount of lists inside the outer
        print(list_2D[i][k], end="")
    print() # next column -> new 'reading line'

# Step 3: Filtering Alpha Characters

# only select alpha characters (letters).
# For each character in a column, check if it’s an alpha character.
# If it is, add it to a temporary string.
# Think about how you can check if a character is an alphabet letter.
temp_str = ""
for k in range(len(list_2D[0])):
    # col k fixed
    for i in range(len(list_2D)):
        if list_2D[i][k].isalpha():
            temp_str += list_2D[i][k]
            print(list_2D[i][k], end="")
    print()
print(temp_str)

# Step 4: Replacing Symbols with Spaces
# Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
# After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space.
# Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.

# Step 5: Constructing the Secret Message
# Combine the filtered and processed characters to form the decoded message.
# Print the decoded message.

temp_str = ""
non_alpha_subseq_count = 0
for k in range(len(list_2D[0])):
    # col k fixed
    for i in range(0,len(list_2D)):
        if list_2D[i][k].isalpha():
            if non_alpha_subseq_count > 0:
                temp_str += " "
            non_alpha_subseq_count = 0
            temp_str += list_2D[i][k]
        else:
            non_alpha_subseq_count += 1
            # print(list_2D[i][k], end="") # prints the non-alpha characters

print(temp_str.strip())
