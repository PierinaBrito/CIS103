#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito


#PART 4

#TAKE HOME 2.1

# 2. Statisticians would like to have a set of functions to compute the median and mode of a
# list of numbers. The median is the number that would appear at the midpoint of a list if it
# were sorted. The mode is the number that appears most frequently in the list. Define these
# functions in a module named stats.py. Also include a function named mean , which
# computes the average of a set of numbers. Each function expects a list of numbers as an
# argument and returns a single number

from stats import mode, median, mean

def main():
    lyst = []

    for i in range(6):
        lyst.append(int(input("Enter a Value for the list: ")))

    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))

if __name__ == "__main__":
    main()
