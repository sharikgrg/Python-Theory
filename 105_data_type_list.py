#list
# list keeps object in order of index
#its defined by []

#example of a list

# list name = [0, 1, 2, 3]
crazy_ex_partners = ['Ross', 'Sara', 'Tommy', 'Dushan']

#print and show type (Read all)
print(crazy_ex_partners)
print(type(crazy_ex_partners))

# get a particular record out (Read One)
#lists are organised with index
print(crazy_ex_partners[0]) # use the index inside square brackets [i]

# How do I print he last one
print(crazy_ex_partners[-1])

# Maybe we want to change a record in specific index?
    # Reassigning index
print(crazy_ex_partners[3])
crazy_ex_partners[3] = 'LANAA !!! (......)DANGER!!!'
print(crazy_ex_partners[3])

# ADD more people to the list (Create one) - append()
print(crazy_ex_partners)
crazy_ex_partners.append('Cyral Figus')
print(crazy_ex_partners)

#Insert in index specific location
crazy_ex_partners.insert(3, 'Malori')
print(crazy_ex_partners)

#Remove someone from the list (Destroy One)
crazy_ex_partners.remove('Malori')# removes based on object
print(crazy_ex_partners)

# Remove using index
crazy_ex_partners.pop() # removes last entry
print(crazy_ex_partners)

crazy_ex_partners.pop(1) # removes based on index
print(crazy_ex_partners)
# Add more people to the list (create one)

#Mixed data and list
    #list can have many data types
hybridlist = 'this is a string', 12, 66, 'hello', [2, 3, 2], [1,2,2]
print (hybridlist)
