#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 1

# WHILE LOOP
# Write a Python program that prints the numbers from 1 to 10 using a
# while loop, but exits the loop when the number reaches 7.
# ◦ Hint: Use the break statement.

# INITIALIZE THE VARIABLE i
i = 1

# START THE WHILE LOOP
while i <= 10:
    #IF THE NUMBER IS 7, EXIT THE LOOP
    if i == 7:
        break

    # PRINT THE NUMBER
    print(i)

    # INCREMENT THE NUMBER
    i += 1
