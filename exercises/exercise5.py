# Assignment Post class
# Use variables, print and different data types
# ask and store the following in variables:
# Name, last_name, age, age_of_mother, 3 skill

# print out information in a formatted manner
# Calculate age difference between response and mother
# Store skills in a list
# print each skill in a formatted way.

# Definition of Formatted
    # a little context text
    # appropriate string formatting like lowercase or upper case or other
name = input('Enter your first Name: ')
last_name = input('Enter your Surname: ')
age = int(input('How old are you? '))
age_of_mother = int(input('How old is your Mother? '))
# skill1 = list(input('List 3 of your skills: ').split(' '))
skill1 = input('List 3 of your skills: ')
skill2 = input('Enter another skill: ')
skill3 = input('Enter last skill: ')
skill_list = [skill1, skill2, skill3]


print(f'Hi, {name.capitalize()} {last_name.capitalize()}, you are {age} years old. Your mother is {age_of_mother-age} years older than you. Your skills are {skill_list[0]},{skill_list[1]} and {skill_list[2]}. !!WOWW!!! You are really skillful')


# print(f'Your skills are {skill1}. You are really skillful')