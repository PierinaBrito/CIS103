#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 3

#TUPLES OPERATION
#◦ Create a tuple with the elements (4, 5, 6, 7, 8).
#◦ Print the first and last elements of the tuple.
#◦ Attempt to change the second element of the tuple and note what happens

# CREATE A TUPLE WITH THE ELEMENTS (4, 5, 6, 7, 8)
my_tuple = (4, 5, 6, 7, 8)

# PRINT THE FIRST AND LAST ELEMENTS OF THE TUPLE
print("First element:", my_tuple[0])
print('Last element:', my_tuple[-1])

# ATTEMPT TO CHANGE THE SECOND ELEMENT OF THE TUPLE
# UNCOMMENT THE LINE BELOW TO SEE THE ERROR

#try:
#    my_tuple[1] = 10
#except TypeError as e:
#    print('Error:', e)

#THE ABOVE LINE WILL RAISE A TYPEERROR BECAUSE TUPLES ARE IMMUTABLE,
#MEANING ONCE A TUPLE IS CREATED, ITS ELEMENTS CANNOT BE MODIFIED.