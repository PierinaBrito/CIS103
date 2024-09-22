#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 2

# STRING REVERSAL
# Write a Python function that takes a string and returns the string reversed.
# Test it with the string "Lab3Python". Hint: Use slicing.

# FUNCTION TO REVERSE A STRING
def reverse_string(s):
    return s[::-1]

# Test the function with the string "Lab3Python"
test_string = "Lab3Python"
reversed_string = reverse_string(test_string)

# PRINT THE RESULT
print("Original string", test_string)
print("Reversed_string", reversed_string)
