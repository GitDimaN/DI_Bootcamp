# Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops

# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

total_cost = 0

while True:
    fam_member_age = input("please specify your next family member's age or 'quit' to finish your order: ")
    if fam_member_age != 'quit':
        fam_member_age = int(fam_member_age)
        if 3 <= fam_member_age <= 12:
            total_cost += 10 
        elif fam_member_age > 12:
            total_cost += 15
    else:
        break
print(f"total ticket cost is: {total_cost}")