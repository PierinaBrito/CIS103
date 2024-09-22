#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 3

# DICTIONARY OPERATION
# Write a Python program that:
# ◦ Creates a dictionary with the following key-value pairs:
# • ‘name’: ‘Alice’, ‘age’: 22, ‘major’: ‘Computer Science’
# • Adds a new key-value pair for the student’s GPA
# • Modifies the student’s age to 23
# • Removes the ‘major’ key from the dictionary
# • Prints all the keys and values from the dictionary


# CREATE A DICTIONARY WITH THE SPECIFIED KEY-VALUE PAIRS
student_info = {
    'name': 'Alice',
    'age': 22,
    'major': 'Computer Science'
}

# ADD A NEW KEY-VALUE PAIR FOR THE STUDENT'S GPA
student_info['GPA'] = 3.8

# MODIFY THE STUDENT'S AGE TO 23
student_info['age'] = 23

# REMOVE THE 'MAYOR' KEY FROM THE DICTIONARY
student_info.pop('major')

# PRINT ALL THE KEYS AND VALUES FROM THE DICTIONARY
for key, value in student_info.items():
    print(f"{key}: {value}")