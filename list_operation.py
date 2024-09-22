#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 2

#LIST OPERATION
#Write a Python program to:
#◦ Create a list of 5 integers of your choice.
#◦ Add a new integer to the list.
#◦ Remove the third element from the list.
#◦ Sort the list in descending order.
#◦ Print the final list.

# Step 1: Create a list of 5 integers
my_list = [10, 20, 30, 40, 50]

# Step 2: Add a new integer to the list
my_list.append(60)

# Step 3: Remove the third element from the list (index 2)
my_list.pop(2)

# Step 4: Sort the list in descending order
my_list.sort(reverse=True)

# Step 5: Print the final list
print(my_list)
