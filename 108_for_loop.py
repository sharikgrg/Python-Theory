
# cars = ['Skoda Felicia Fun', 'Fiat Panda 4X4', 'Mustang Ford', 'Corvette']

#Syntax

# for <placeholder> in <iteratable>: # Don't forget the colon
    # block of code
    # Indented gets run every iteration

# for car in cars:
#     print('hey :D')
#     print(car)
#
# embeded_list = [['filipe', 'francis'], ['Moustapha', 'David', 'Julienne']]
#
# for data in embeded_list:
#     print(data)
#     for names in data:
#         print(names)

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'complete modules': ['sword', 'augmneted senses', 'no face', 'no name']
}
count_1 = 1 # adding the numbers
for key in student1:
    print(count_1, key, ': ',student1[key])
    count_1 += 1