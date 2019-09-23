# String
# these are a list of characters put together
# defined by '' or ""

my_string = 'Amazing Grilled Fish'
print(type(my_string))
#you can print it
print(my_string)

# Join of strings - concatenation
first_name = 'Boris'
last_name = 'Becker'
print(first_name[0]) # string is a character sp it behaves like a list
#concatenating 3 strings
full_name = first_name + ' ' + last_name
print(full_name)
print('string',14)

# Interpolation
name = 'Rachel'
welcome_message = 'hey there,  how youuuu doinn? ;)'
print(f'hey there, {name} how youuuu doinn? ;)')
# palce an f on the left/beginnning of the string
# then you can use {} to interpolated python variable inside

# Useful methods for strings
my_string = 'Hello this is an amazing string      '

# count() is a method so needs to be added as with .
print(my_string.count('i'))
print(my_string.count(' '))

# strip() # removes trailing white spaces
print(my_string.strip())

#len() is a function length
print(len(my_string))

#.lower() lower cases
print(my_string.lower())

#.upper() upper cases
print(my_string.upper())

#.capitalize() capitalises first letter of sentence
print(my_string.strip().capitalize())

# .replace(arg_int,arg_two) replaces words or letters
print(my_string.replace('an', 'the'))

# .split(arg) --> list
print(my_string.split(' '))
