# Define the following variable
# name, last name, age, eye_colour, hair_colour

# Prompt user for input and reassign these

# Print them back to the user as conversation
# Eg: Hello Jack! Welcome, your age is 26, you eyes are green and your hair_colour are grey

name = input('What is your name?')
last_name = input('What is your surname?')
age = input('What is your age?')
eye_colour = input('What is the colour of your eye?')
hair_colour = input('What is the colour of your hair?')
print('Hello',name.capitalize(), f'{last_name.capitalize()}!', 'Welcome, your age is', f'{age},', 'your eyes are', eye_colour, 'and your hair is', hair_colour)
print(f'Hello {name} {last_name}, Welcome!, your age is')
print('You were born in', 2019 - int(age))