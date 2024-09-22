#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 1

# NESTED LOOP
#  Write a Python program that uses nested loops to generate the
# following pattern:
# *
# **
# ***
# ****
# *****


# OUTER LOOP FOR THE NUMBER OF ROWS
for i in range(1, 6):
    # INNER LOOP FOR PRINTING '*' IN EACH ROW
    for j in range(i):
        print('*', end='') # PRINT '*' WITHOUT A NEW LINE
    print()  # MOVE TO THE NEXT LINE AFTER INNER LOOP
