#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito


#PART 4

#TAKE HOME 2.0

# 2. Statisticians would like to have a set of functions to compute the median and mode of a
# list of numbers. The median is the number that would appear at the midpoint of a list if it
# were sorted. The mode is the number that appears most frequently in the list. Define these
# functions in a module named stats.py. Also include a function named mean , which
# computes the average of a set of numbers. Each function expects a list of numbers as an
# argument and returns a single number.



# CALCULATE THE MODE OF THE LIST
def mode(numbers):
    frequency_dict = {}
    for num in numbers:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    mode_value = max(frequency_dict, key=frequency_dict.get)
    return mode_value

# CALCULATE THE MEDIAN OF THE LIST
def median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    #IF THE LENGTH IS EVEN, TAKE AVERAGE OF THE MIDDLE TWO ELEMENTS
    if length % 2 == 0:
        middle1 = sorted_numbers[length // 2 - 1]
        middle2 = sorted_numbers[length // 2]
        median_value = (middle1 + middle2) / 2
    #IF THE LENGTH IS ODD, TAKE THE MIDDLE ELEMENT
    else:
        median_value = sorted_numbers[length // 2]

    return median_value

# CALCULATE THE MEAN (AVERAGE) OF THE LIST
def mean(numbers):
    mean_value = sum(numbers) / len(numbers)
    return mean_value
