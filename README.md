CIS 103: Fundamentals of Programming
Lab 1: Python Loops and Object Types

Objective:
The purpose of this lab is to practice and reinforce Python programming concepts related to
loops (while, for, nested loops), string operations, lists, tuples, and dictionaries.


Part 1: Looping Constructs

• While Loop: Write a Python program that prints the numbers from 1 to 10 using a
while loop, but exits the loop when the number reaches 7.
◦ Hint: Use the break statement.


• For Loop: Write a Python program that iterates over the string "CIS103Lab3"
and prints each character, one by one, followed by its index in the string.


• Nested Loop: Write a Python program that uses nested loops to generate the
following pattern:
*
**
***
****
*****


• Break and Continue: Modify the program from Exercise 1. This time, use the
continue statement to skip the number 5, but the program should still print
numbers from 1 to 10, breaking at 7.


Part 2: Strings and List Operations

• String Reversal: Write a Python function that takes a string and returns the string
reversed. Test it with the string "Lab3Python". Hint: Use slicing.

• List Operations: Write a Python program to:
◦ Create a list of 5 integers of your choice.
◦ Add a new integer to the list.
◦ Remove the third element from the list.
◦ Sort the list in descending order.
◦ Print the final list.


Part 3: Tuples and Dictionaries


• Tuple Operations:
◦ Create a tuple with the elements (4, 5, 6, 7, 8).
◦ Print the first and last elements of the tuple.
◦ Attempt to change the second element of the tuple and note what happens.


• Dictionary Operations: Write a Python program that:
◦ Creates a dictionary with the following key-value pairs:
• ‘name’: ‘Alice’, ‘age’: 22, ‘major’: ‘Computer Science’
• Adds a new key-value pair for the student’s GPA
• Modifies the student’s age to 23
• Removes the ‘major’ key from the dictionary
• Prints all the keys and values from the dictionary


Part 4: Take Home

1. Write a program that takes the radius of a sphere (a floating-point number) as input and
outputs the sphere’s diameter, circumference, surface area, and volume.

2. Statisticians would like to have a set of functions to compute the median and mode of a
list of numbers. The median is the number that would appear at the midpoint of a list if it
were sorted. The mode is the number that appears most frequently in the list. Define these
functions in a module named stats.py. Also include a function named mean , which
computes the average of a set of numbers. Each function expects a list of numbers as an
argument and returns a single number.
