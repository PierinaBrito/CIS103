#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 1

# BREAK AND CONTINUE
# Modify the program from Exercise 1. This time, use the
# continue statement to skip the number 5, but the program should still print
# numbers from 1 to 10, breaking at 7

# INITIALIZE THE VARIABLE i
i = 1

# START THE WHILE LOOP
while i <= 10:
    # SKIP THE NUMBER 5
    if i == 5:
        i += 1
        continue

    # BREAK THE LOOP WHEN THE NUMBER IS 7
    if i == 7:
        break

    # PRINT THE CURRENT NUMBER
    print(i)

    # INCREMENT THE NUMBER
    i += 1
