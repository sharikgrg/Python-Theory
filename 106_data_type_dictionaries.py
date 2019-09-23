# Dictionaries
# all fun and games keeping our crazy ex list... but we also need more info
# introducing dictionaries

#dictionaries are defined using{}
#They hare organised with keys that point to values
# much like looking up spmething on a dictionary or information about a contact on our phones.
    # thus in our phone, the contact fiipe paiva will hold lots of info for
    #this entry. could be the phone number, work number, email address and so on...

#Syntax
# dict_name = {'example_key':'value'}

#Defining a simple dictionary with two keys
dictionary_crazy_ex = {
    'Carolina': 'She was actually nice',
    'Arthur': 'bit of a drinker',
}

print(dictionary_crazy_ex)
print(type(dictionary_crazy_ex))

#Accessing values-  use the key!
print(dictionary_crazy_ex['Carolina'])
print(dictionary_crazy_ex['Arthur'])

# Adding a new key, pair value
dictionary_crazy_ex['Kile'] = 'Likes Monster'
print(dictionary_crazy_ex)

dictionary_crazy_ex['Kile'] = 'Really Likes Monster'
print(dictionary_crazy_ex)

# Get out all os the keys
print(dictionary_crazy_ex.keys())

# Get out all of the values

print(dictionary_crazy_ex.values())

# remove item from dictionary
dictionary_crazy_ex.pop('Kile')
print(dictionary_crazy_ex)

#Better example of a dictionary:

crazy1 = {
    'name': 'Carolina',
    'phone': '07842715517',
    'address': 'Location 1, at places',
    'known places to avoid': ['Milan','Lisbon', 'Tavira']
}