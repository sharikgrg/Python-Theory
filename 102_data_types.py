# Numerical Data Types
# - Int, long, float, complex
# These are numerical data types which we can use numerical operators.

# Complex and long we don't use as much
# complex brings an imaginary type of number
# long - are integers of unlimited size
# Floats

# int - stmads for integers
# Whole numbers
my_int = 20
print(my_int)
print(type(my_int))

# Operator - Add, Subtract, multiply and devide

print(4+3)
print(4-3)
print(4/2) # decimals get automatically converted to float
print(4//2) # keeps it as integer/ drops the decimal
print(4*2)
print(3**2) # square

# Modules looks for the number of remainder
# % #
print(10%3) ## --> 3*3 =9, so 1 is the remainder

# Comparison Operators ## --> boolean value

# < / > - Bigger and Smaller than
# <= - Smaller than or equal
# >= Bigger than or equal
# != Not equal
# is and is not

my_variable1 = 10
my_variable2 = 13

# example of using operators

print(my_variable1== my_variable2) # output is false
print(my_variable1 > my_variable2)
print(my_variable1 < my_variable2)
print(my_variable1 >= my_variable2)
print(my_variable1 != my_variable2)
print(my_variable1 is my_variable2)
print(my_variable1 is not my_variable2)

# Boolean Values
# Define by either True or False
print(type(True))
print(type(False))
print (0 == False)
print(1 == True)

## None
print(None)
print(type(None))
print(bool(None))

#Logical And & Or
a = True
b = False
print('Logical and & or -------')
# Using *and* both sides have to be true for it to result in true
print(a and True)
print((1==1) and (True))
print((1==1) and False)

#Use or only one side needs to be true
print('this will print true-----')
print(True or False)
print(True or 1==2)
print('this will print false -----------')
print(False or 1==2)