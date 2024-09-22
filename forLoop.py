#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 1

# FOR LOOP
# Write a Python program that iterates over the string "CIS103Lab3"
# and prints each character, one by one, followed by its index in the string.

# INITIALIZE THE STRING
string = "CIS103Lab3"

# THE ENUMERATE FUNCTION HELP TO GET BOTH THE INDEX AND THE CHARACTER
for index, char in enumerate(string):
    print(f"Character: {char}, Index: {index}")
