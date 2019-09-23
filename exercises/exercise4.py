# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # Start, Middle and End
story1 = {
    'Start': 'Once upon a time,',
    'Middle': 'I was born.',
    'End': 'The end.'
}

#2 - Print the entire dictionary
print(story1)

#3 - Print the type of your dictionary
print(type(story1))

#4 - Print only the keys
print(story1.keys())

#4 - print only the values
print(story1.values())

#5 - print the individual values using the keys
print(story1['Start'])
print(story1['Middle'])
print(story1['End'])

#6 Now lets add a new key:value pair.
story1['Continuation'] = 'Life carried on.'
print(story1)
print(story1['Start'])
print(story1['Middle'])
print(story1['Continuation'])
print(story1['End'])

