# Assignment 2 for post class
#
# define an empty dictionary# name_dict = {}

# Prompt user for inout for a story
# it should have:
    # hero, beginning, middle, end
    # 2 other things to define the part of the story
    # add each response to the dictionary under an appropriate key

# Print out the dicitionary information in an ordered way so we can read the story
hero = input('Choose a name for your champion: ')
adj = input('Word to describe a warrior: ')
adj2 = input('Pick adjective for a situation: ')
sit1 = input('what insect are you afraid of? ')
sit2 =  input('Which person are you scared of? ')
sit3 = input("Pick a number that's bigger than a 100: ")
story = {
    'Name': hero,
    'Second': adj,
    'beginning': adj2,
    'middle': sit1,
    'mend': sit2,
    'end': sit3
}

print(f'{story["Name"].capitalize()} was a {story["Second"].upper()} warrior.')
print(f' He never hid away from {story["beginning"]} situations. ')
print(f'He killed many {story["middle"]} and also beat up many {story["mend"]}. He lived till {story["end"]}. ')

# John was a --- warior. He never hid away from --- situation adjective. He killed many ---. He beat --- up